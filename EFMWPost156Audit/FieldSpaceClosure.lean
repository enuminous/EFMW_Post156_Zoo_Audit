import RequestProject.FieldSpace.Gluing
import RequestProject.FieldSpace.Conservation

/-!
# FieldSpace source-closure audit

Support lemmas below are for an explicitly proposed algebraic completion. They
do not identify a physical current or stress tensor. The counterexample records
why shared-component source comparisons do not imply the full-vector gluing
premise of the imported theorem. No conclusion is installed as a new axiom.
-/

namespace EFMWPost156Audit.FieldSpaceClosure

open FieldSpace

section MixedSupport

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- Proposed amplitude-product current, with a typed vector/tensor coefficient. -/
noncomputable def mixedCurrent (a b c : ℝ) (coefficient : V) : V :=
  (a * b * c) • coefficient

/-- A nontrivial construction satisfying all three required zero-amplitude slices. -/
theorem mixedCurrent_null_slice (a b c : ℝ) (coefficient : V)
    (h : a = 0 ∨ b = 0 ∨ c = 0) : mixedCurrent a b c coefficient = 0 := by
  rcases h with h | h | h <;> simp [mixedCurrent, h]

/-- Explicit pair terms plus a genuine three-amplitude remainder. -/
noncomputable def mixedStress (a b c : ℝ) (ab ac bc abc : V) : V :=
  (a * b) • ab + (a * c) • ac + (b * c) • bc + mixedCurrent a b c abc

theorem mixedStress_pair_restriction (a b : ℝ) (ab ac bc abc : V) :
    mixedStress a b 0 ab ac bc abc = (a * b) • ab := by
  simp [mixedStress, mixedCurrent]

/-- Different third-chart coefficients cannot affect the retained pair slice. -/
theorem mixedStress_chart_independent (a b : ℝ) (ab ac bc abc ad bd abd : V) :
    mixedStress a b 0 ab ac bc abc = mixedStress a b 0 ab ad bd abd := by
  simp [mixedStress_pair_restriction]

theorem mixedCurrent_nontrivial : mixedCurrent 1 1 1 (1 : ℝ) ≠ 0 := by
  norm_num [mixedCurrent]

end MixedSupport

/-- What the source's overlap audit actually compares: equations for shared sectors. -/
def SharedCompatible (k : ℕ)
    (f : Finset Sector → (Sector → ℚ) → Sector → ℚ) : Prop :=
  ∀ A B : Finset Sector, A.card = k → B.card = k →
    ∀ φ : Sector → ℚ, ∀ s ∈ A ∩ B,
      f A (FieldSpace.restrict (A ∩ B) φ) s =
      f B (FieldSpace.restrict (A ∩ B) φ) s

/-- Source-shaped specialization: only λ_TF = 1 remains. Missing equation
components are padded with zero. On FWT the T equation is φ_F; on FWI it is absent. -/
def zeroPaddedChart (A : Finset Sector) (φ : Sector → ℚ) (s : Sector) : ℚ :=
  if s ∈ A ∧ s = Sector.T then φ Sector.F else 0

theorem zeroPaddedChart_shared_compatible : SharedCompatible 3 zeroPaddedChart := by
  intro A B _ _ φ s hs
  have ha : s ∈ A := (Finset.mem_inter.mp hs).1
  have hb : s ∈ B := (Finset.mem_inter.mp hs).2
  simp [zeroPaddedChart, ha, hb]

/-- A concrete witness to the missing bridge, using two real source chart labels. -/
theorem zeroPaddedChart_not_gluingCompatible :
    ¬ FieldSpace.GluingCompatible 3 zeroPaddedChart := by
  intro h
  have heq := h {Sector.F, Sector.W, Sector.T} {Sector.F, Sector.W, Sector.I}
    (by decide) (by decide) (fun _ => (1 : ℚ))
  have ht := congrFun heq Sector.T
  norm_num [zeroPaddedChart, FieldSpace.restrict] at ht
  exact (by decide : Sector.T ≠ Sector.I) (ht (by decide) (by decide))

/-- The generic gluing theorem cannot supply a full-vector extension of this
zero-padded encoding, even though every shared-component comparison passes. -/
theorem zeroPaddedChart_no_full_extension :
    ¬ ∃ F : (Sector → ℚ) → Sector → ℚ, FieldSpace.RestrictsTo 3 F zeroPaddedChart := by
  rintro ⟨F, hF⟩
  exact zeroPaddedChart_not_gluingCompatible
    (FieldSpace.gluingCompatible_of_restrictsTo hF)

/-- The shared-component predicate is strictly weaker than full-vector gluing. -/
theorem shared_compatibility_insufficient :
    ∃ f : Finset Sector → (Sector → ℚ) → Sector → ℚ,
      SharedCompatible 3 f ∧ ¬ FieldSpace.GluingCompatible 3 f :=
  ⟨zeroPaddedChart, zeroPaddedChart_shared_compatible,
    zeroPaddedChart_not_gluingCompatible⟩

/-- On a removed scalar slice, the stress contains -g V(0). A removed gauge
contributes zero. Identical mixed pair stress does not remove that difference. -/
theorem vacuum_stress_overlap_iff (common metric vacuum mixed : ℝ) :
    common - metric * vacuum + mixed = common + mixed ↔ metric * vacuum = 0 := by
  constructor <;> intro h <;> linarith

theorem vacuum_zero_required (common metric vacuum mixed : ℝ) (hg : metric ≠ 0)
    (h : common - metric * vacuum + mixed = common + mixed) : vacuum = 0 := by
  have hm := (vacuum_stress_overlap_iff common metric vacuum mixed).mp h
  exact (mul_eq_zero.mp hm).resolve_left hg

end EFMWPost156Audit.FieldSpaceClosure
