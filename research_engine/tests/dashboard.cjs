// CI-only UI check. The engine itself has no Node or Playwright dependency.
const assert = require('node:assert/strict');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');

(async () => {
  const browser = await chromium.launch({headless: true});
  try {
    const page = await browser.newPage({viewport: {width: 1440, height: 1100}});
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
    assert.equal(await page.locator('#equation option').count(), 102);
    assert.equal(await page.locator('#triplet option').count(), 165);
    assert.equal(await page.locator('#animal option').count(), 46);
    assert.equal(await page.locator('#slotId').textContent(), 'ME-002/FS-EFM/TORTOISE');
    assert.equal(await page.locator('#slotStatus').textContent(), 'proposed');
    assert.match(await page.locator('#slotRuns').textContent(), /3 recorded attempts/);
    await page.selectOption('#equation', 'ME-012');
    assert.equal(await page.locator('#slotStatus').textContent(), 'unknown');
    assert.match(await page.locator('#slotRuns').textContent(), /Unrun/);
    await page.fill('#search', 'placebo');
    await page.locator('#searchResults button').filter({hasText: 'BAT'}).click();
    assert.equal(await page.inputValue('#animal'), 'BAT');
    await page.getByRole('tab', {name: 'Execution ledger'}).click();
    assert.equal(await page.locator('#runsTable tbody tr').count(), 48);
    await page.locator('#runsTable tbody tr').last().getByRole('button').click();
    assert.match(await page.locator('#runDetail').textContent(), /must|Expected/);
    const downloadPromise = page.waitForEvent('download');
    await page.getByRole('button', {name: 'Download status JSON'}).click();
    assert.equal((await downloadPromise).suggestedFilename(), 'efmw-status.json');
    await page.getByRole('tab', {name: 'Next work'}).click();
    assert.equal(await page.locator('#sources .source').count(), 9);
    await page.getByRole('tab', {name: 'Explore the atlas'}).click();
    await page.fill('#search', '');
    await page.selectOption('#equation', 'ME-002');
    await page.selectOption('#animal', 'TORTOISE');
    if (process.argv[3]) await page.screenshot({path: path.join(process.argv[3], 'desktop.png'), fullPage: true});
    await page.setViewportSize({width: 390, height: 844});
    assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), true, 'mobile horizontal overflow');
    assert.equal(await page.locator('#eqPanel').isVisible(), true);
    if (process.argv[3]) await page.screenshot({path: path.join(process.argv[3], 'mobile.png'), fullPage: true});
    assert.deepEqual(errors, []);
    console.log('PASS: 102/165/46 selectors; mappings; search; 48 runs; retained error; download; sources; mobile width; no JS errors.');
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
