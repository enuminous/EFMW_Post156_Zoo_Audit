# Frozen FieldSpace input

- Repository: https://github.com/enuminous/Einsteinian-156-Aristotle
- Commit: `7e60205d2370c335ebe2cafe89d6e0bbe842ba01`
- Original path: `source/EFMW_165_field_equations.txt`
- Git blob: `ac6313fe4a2b02a28ac8fb34519c5f96f6ea2bd8`
- SHA-256: `7e263c783d20b8c4556b4bbb631d4bc8a0e49aded7450ecf1b3ed78e3ebff451`
- Size: 64,859 bytes

The equation file is copied byte for byte. The audit checks its Git blob hash
before parsing. `UPSTREAM_GLUING_AUDIT.md` and
`UPSTREAM_GLOBAL_RECONSTRUCTION.md` preserve the upstream interpretation as
historical inputs. Their full-source reconstruction conclusion is not adopted
by this audit; see `docs/FIELDSPACE_CLOSURE_AUDIT.md` for the missing hypothesis.

The Lean library is imported as a Git dependency at the same immutable commit.
`lake-manifest.json` records every resolved dependency, including Mathlib
`8f9d9cff6bd728b17a24e163c9402775d9e6a365` (v4.28.0).

The Python parser is an explicit translation boundary, not a verified parser.
Its fail-closed syntax checks and mutation tests do not turn source text into
a kernel-checked PDE model. The Lean counterexample is a source-shaped
specialization; the proposed mixed terms are additional algebraic definitions.

No upstream source file or theorem has been rewritten to make the result pass.
