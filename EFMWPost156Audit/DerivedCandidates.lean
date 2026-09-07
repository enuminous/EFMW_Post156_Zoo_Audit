import Mathlib

/-!
# EFMW post-156 audit candidates T177–T181

These are self-contained mathematical targets using the same algebraic forms
audited in the EFMW repositories.  They are intentionally separated from the
upstream Aristotle namespace so this audit can test the identities independently.

AUDIT STATUS AT PACKAGE CREATION: DERIVED — LEAN PENDING.
No claim is made here that the file has already passed `lake build`.
-/

namespace EFMWPost156Audit

open Real

noncomputable def phaseSpeed (c alpha : ℝ) : ℝ :=
  c / Real.sqrt (1 - alpha ^ 2)

/-- T177: scalar phase speed cannot distinguish the sign of alpha. -/
theorem phaseSpeed_neg (c alpha : ℝ) :
    phaseSpeed c (-alpha) = phaseSpeed c alpha := by
  simp [phaseSpeed]

/-- T178: a nontrivial real plane-wave dispersion solution forces alpha^2 < 1. -/
theorem real_wave_admissibility
    {alpha omega c k : ℝ}
    (hrel : (1 - alpha ^ 2) * omega ^ 2 = c ^ 2 * k ^ 2)
    (homega : omega ≠ 0) (hc : c ≠ 0) (hk : k ≠ 0) :
    alpha ^ 2 < 1 := by
  have hω2 : 0 < omega ^ 2 := sq_pos_of_ne_zero homega
  have hc2 : 0 < c ^ 2 := sq_pos_of_ne_zero hc
  have hk2 : 0 < k ^ 2 := sq_pos_of_ne_zero hk
  have hrhs : 0 < c ^ 2 * k ^ 2 := mul_pos hc2 hk2
  have hlhs : 0 < (1 - alpha ^ 2) * omega ^ 2 := by
    rw [hrel]
    exact hrhs
  have hcoef : 0 < 1 - alpha ^ 2 := by
    by_contra hnot
    have hle : 1 - alpha ^ 2 ≤ 0 := le_of_not_gt hnot
    have : (1 - alpha ^ 2) * omega ^ 2 ≤ 0 :=
      mul_nonpos_of_nonpos_of_nonneg hle (le_of_lt hω2)
    linarith
  linarith

/-- T179: exact model speed can be inverted to recover alpha^2. -/
theorem phaseSpeed_inversion
    {c alpha v : ℝ}
    (hc : 0 < c) (halpha : alpha ^ 2 < 1)
    (hv : v = phaseSpeed c alpha) :
    alpha ^ 2 = 1 - (c / v) ^ 2 := by
  have hpos : 0 < 1 - alpha ^ 2 := by linarith
  have hs : 0 < Real.sqrt (1 - alpha ^ 2) := Real.sqrt_pos.mpr hpos
  have hsq : Real.sqrt (1 - alpha ^ 2) ^ 2 = 1 - alpha ^ 2 :=
    Real.sq_sqrt (le_of_lt hpos)
  have hcv : c / v = Real.sqrt (1 - alpha ^ 2) := by
    rw [hv, phaseSpeed]
    field_simp [ne_of_gt hc, ne_of_gt hs]
  rw [hcv, hsq]
  ring

noncomputable def friedmannLCDM
    (Gnewton rho Lam k a : ℝ) : ℝ :=
  (8 * Real.pi * Gnewton / 3) * rho + Lam / 3 - k / a ^ 2

noncomputable def friedmannEFMW
    (Gnewton rho Lam k a OmegaU : ℝ) : ℝ :=
  friedmannLCDM Gnewton rho Lam k a + OmegaU ^ 2 / a ^ 2

/-- T180: the current Friedmann extension cannot distinguish rotation sign. -/
theorem friedmann_rotation_sign_degeneracy
    (Gnewton rho Lam k a OmegaU : ℝ) :
    friedmannEFMW Gnewton rho Lam k a (-OmegaU) =
      friedmannEFMW Gnewton rho Lam k a OmegaU := by
  simp [friedmannEFMW]

/-- T181: constant residual rotation is algebraically degenerate with curvature shift. -/
theorem friedmann_rotation_curvature_degeneracy
    (Gnewton rho Lam k a OmegaU : ℝ) :
    friedmannEFMW Gnewton rho Lam k a OmegaU =
      friedmannLCDM Gnewton rho Lam (k - OmegaU ^ 2) a := by
  simp [friedmannEFMW, friedmannLCDM]
  ring

end EFMWPost156Audit
