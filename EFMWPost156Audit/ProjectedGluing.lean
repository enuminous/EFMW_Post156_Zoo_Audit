import EFMWPost156Audit.FieldSpaceClosure

/-!
# Gluing with equation-component restriction

Input fields and output equations both restrict to an overlap. The uniqueness
class counts an equation's own sector among the allowed k sectors. This is a
deliberate replacement specification, not a proof of the stronger zero-padded
full-vector claim rejected in FieldSpaceClosure.
-/

namespace EFMWPost156Audit.ProjectedGluing

open Finset FieldSpace

variable {ι R M : Type*} [DecidableEq ι] [Zero R] [AddCommGroup M]

/-- Only equation components present in both charts are compared. -/
def ProjectedCompatible (k : ℕ) (f : Finset ι → (ι → R) → ι → M) : Prop :=
  ∀ A B : Finset ι, A.card = k → B.card = k → ∀ φ : ι → R, ∀ s ∈ A ∩ B,
    f A (restrict (A ∩ B) φ) s = f B (restrict (A ∩ B) φ) s

/-- A global equation family reproduces precisely the components a chart has. -/
def ProjectedRestrictsTo (k : ℕ) (F : (ι → R) → ι → M)
    (f : Finset ι → (ι → R) → ι → M) : Prop :=
  ∀ T : Finset ι, T.card = k → ∀ φ : ι → R, ∀ s ∈ T,
    F (restrict T φ) s = f T (restrict T φ) s

/-- Every term in component s involves at most k sectors when s is counted.
In particular, a triplet equation may depend on s and at most two other sectors.
This excludes terms in three other sectors that its triplet observations miss. -/
def IsComponentKBody [Fintype ι] (k : ℕ) (F : (ι → R) → ι → M) : Prop :=
  ∀ s, ∃ h : Finset ι → (ι → R) → M, (∀ S, DependsOn S (h S)) ∧
    ∀ φ, F φ s = ∑ S ∈ univ.filter (fun S : Finset ι => (insert s S).card ≤ k), h S φ

/-- The component predicate is exactly equality after restricting outputs too. -/
theorem projectedCompatible_iff_output_restriction {k : ℕ}
    (f : Finset ι → (ι → R) → ι → M) :
    ProjectedCompatible k f ↔
      ∀ A B : Finset ι, A.card = k → B.card = k → ∀ φ : ι → R,
        restrict (A ∩ B) (f A (restrict (A ∩ B) φ)) =
        restrict (A ∩ B) (f B (restrict (A ∩ B) φ)) := by
  constructor
  · intro h A B hA hB φ
    funext s
    by_cases hs : s ∈ A ∩ B
    · simpa only [restrict, if_pos hs] using h A B hA hB φ s hs
    · simp only [restrict, if_neg hs]
  · intro h A B hA hB φ s hs
    have e := congrFun (h A B hA hB φ) s
    simpa only [restrict, if_pos hs] using e

/-- Boolean-lattice inversion with the equation label included in the bound. -/
theorem sum_mobius_component (k : ℕ) (s : ι) [Fintype ι]
    {a : Finset ι → M} {T : Finset ι} (hT : (insert s T).card ≤ k)
    (ha : ∀ U, a U = a (U ∩ T)) :
    ∑ S ∈ univ.filter (fun S : Finset ι => (insert s S).card ≤ k), mobius a S = a T := by
  rw [← sum_subset (s₁ := T.powerset), sum_mobius_powerset]
  · intro S hS
    have hsub : insert s S ⊆ insert s T := by
      intro i hi
      rcases mem_insert.mp hi with rfl | hi
      · exact mem_insert_self s T
      · exact mem_insert_of_mem ((mem_powerset.mp hS) hi)
    simpa using (card_le_card hsub).trans hT
  · intro S _ hS
    exact mobius_eq_zero_of_not_subset ha (fun h => hS (mem_powerset.mpr h))

theorem IsComponentKBody.eq_sum_mobius [Fintype ι] {k : ℕ}
    {F : (ι → R) → ι → M} (hF : IsComponentKBody k F) (φ : ι → R) (s : ι) :
    F φ s = ∑ S ∈ univ.filter (fun S : Finset ι => (insert s S).card ≤ k),
      mobius (fun U => F (restrict U φ) s) S := by
  obtain ⟨h, hdep, hsum⟩ := hF s
  simp only [hsum, mobius_sum]
  rw [sum_comm]
  refine sum_congr rfl fun S0 hS0 => ?_
  rw [sum_mobius_component k s (T := S0) (mem_filter.mp hS0).2, ← hdep]
  intro U
  rw [hdep S0 (restrict U φ), restrict_restrict, hdep S0 (restrict (U ∩ S0) φ),
    restrict_restrict, ← inter_assoc, inter_comm S0 U, inter_assoc, inter_self]

/-- Every projected global extension supplies the projected overlap condition. -/
theorem projectedCompatible_of_restrictsTo {k : ℕ} {F : (ι → R) → ι → M}
    {f : Finset ι → (ι → R) → ι → M} (hF : ProjectedRestrictsTo k F f) :
    ProjectedCompatible k f := by
  intro A B hA hB φ s hs
  have eA : restrict A (restrict (A ∩ B) φ) = restrict (A ∩ B) φ :=
    restrict_of_superset inter_subset_left φ
  have eB : restrict B (restrict (A ∩ B) φ) = restrict (A ∩ B) φ :=
    restrict_of_superset inter_subset_right φ
  have a := hF A hA (restrict (A ∩ B) φ) s (mem_inter.mp hs).1
  have b := hF B hB (restrict (A ∩ B) φ) s (mem_inter.mp hs).2
  rw [eA] at a
  rw [eB] at b
  exact a.symm.trans b

/-- Construct the extension by Möbius inversion, choosing for each component and
support a containing chart that also contains the equation's own sector. -/
theorem exists_componentKBody_of_projectedCompatible [Fintype ι] {k : ℕ}
    (hk : k ≤ Fintype.card ι) {f : Finset ι → (ι → R) → ι → M}
    (hf : ProjectedCompatible k f) :
    ∃ F, IsComponentKBody k F ∧ ProjectedRestrictsTo k F f := by
  have hex : ∀ (s : ι) (S : Finset ι), ∃ T : Finset ι,
      (insert s S).card ≤ k → insert s S ⊆ T ∧ T.card = k := by
    intro s S
    by_cases hS : (insert s S).card ≤ k
    · obtain ⟨T, hST, hT⟩ := exists_superset_card_eq hS hk
      exact ⟨T, fun _ => ⟨hST, hT⟩⟩
    · exact ⟨S, fun h => absurd h hS⟩
  choose τ hτ using hex
  let loc : ι → Finset ι → (ι → R) → M :=
    fun s S φ => mobius (fun U => f (τ s S) (restrict U φ) s) S
  refine ⟨fun φ s => ∑ S ∈ univ.filter (fun S : Finset ι => (insert s S).card ≤ k),
    loc s S φ, ?_, ?_⟩
  · intro s
    exact ⟨loc s, fun S φ => mobius_congr fun U hU => by
      rw [restrict_of_subset hU], fun _ => rfl⟩
  · intro T hT φ s hs
    have ha : ∀ (X U : Finset ι), f X (restrict U (restrict T φ)) s =
        f X (restrict (U ∩ T) (restrict T φ)) s := by
      intro X U
      rw [restrict_restrict, restrict_restrict, inter_assoc, inter_self]
    have key : ∀ S ∈ univ.filter (fun S : Finset ι => (insert s S).card ≤ k),
        loc s S (restrict T φ) = mobius (fun U => f T (restrict U (restrict T φ)) s) S := by
      intro S hS
      have hS' := (mem_filter.mp hS).2
      by_cases hST : S ⊆ T
      · refine mobius_congr fun U hU => ?_
        have hsub : U ⊆ τ s S ∩ T := subset_inter
          (fun i hi => (hτ s S hS').1 (mem_insert_of_mem (hU hi))) (hU.trans hST)
        have hsmem : s ∈ τ s S ∩ T :=
          mem_inter.mpr ⟨(hτ s S hS').1 (mem_insert_self s S), hs⟩
        have e := hf (τ s S) T (hτ s S hS').2 hT (restrict U φ) s hsmem
        rw [restrict_of_superset hsub] at e
        rw [restrict_of_subset (hU.trans hST), e]
      · show mobius (fun U => f (τ s S) (restrict U (restrict T φ)) s) S = _
        rw [mobius_eq_zero_of_not_subset (ha (τ s S)) hST,
          mobius_eq_zero_of_not_subset (ha T) hST]
    have hbound : (insert s T).card ≤ k := by simp [insert_eq_of_mem hs, hT]
    simp only
    rw [sum_congr rfl key, sum_mobius_component k s hbound (ha T),
      restrict_of_subset subset_rfl]

theorem projected_atlas_gluing [Fintype ι] {k : ℕ} (hk : k ≤ Fintype.card ι)
    (f : Finset ι → (ι → R) → ι → M) :
    ProjectedCompatible k f ↔ ∃ F, IsComponentKBody k F ∧ ProjectedRestrictsTo k F f :=
  ⟨exists_componentKBody_of_projectedCompatible hk,
    fun ⟨_, _, hF⟩ => projectedCompatible_of_restrictsTo hF⟩

/-- Uniqueness holds in the stated component-indexed interaction class. -/
theorem projected_atlas_gluing_unique [Fintype ι] {k : ℕ} (hk : k ≤ Fintype.card ι)
    {F G : (ι → R) → ι → M} (hF : IsComponentKBody k F) (hG : IsComponentKBody k G)
    (h : ∀ T : Finset ι, T.card = k → ∀ φ, ∀ s ∈ T,
      F (restrict T φ) s = G (restrict T φ) s) : F = G := by
  funext φ s
  rw [hF.eq_sum_mobius, hG.eq_sum_mobius]
  refine sum_congr rfl fun S hS => mobius_congr fun U hU => ?_
  obtain ⟨T, hST, hT⟩ := exists_superset_card_eq (mem_filter.mp hS).2 hk
  have hUT : U ⊆ T := fun i hi => hST (mem_insert_of_mem (hU hi))
  have hs : s ∈ T := hST (mem_insert_self s S)
  have e : restrict T (restrict U φ) = restrict U φ := restrict_of_superset hUT φ
  rw [← e]
  exact h T hT _ s hs

/-- Repaired FS-C01 for the 165-chart atlas, with both restriction maps explicit. -/
theorem fieldSpace_projected_atlas_gluing (f : Finset Sector → (Sector → R) → Sector → M) :
    ProjectedCompatible 3 f ↔ ∃! F : (Sector → R) → Sector → M,
      IsComponentKBody 3 F ∧ ProjectedRestrictsTo 3 F f := by
  have hk : 3 ≤ Fintype.card Sector := by simp [card_sector]
  rw [projected_atlas_gluing hk]
  refine ⟨fun ⟨F, hF⟩ => ⟨F, hF, fun G hG =>
    projected_atlas_gluing_unique hk hG.1 hF.1 ?_⟩, fun ⟨F, hF, _⟩ => ⟨F, hF⟩⟩
  intro T hT φ s hs
  rw [hG.2 T hT φ s hs, hF.2 T hT φ s hs]

open FieldSpaceClosure

/-- The previously rejected full-vector example has a unique repaired extension. -/
theorem zeroPaddedChart_has_unique_projected_extension :
    ∃! F : (Sector → ℚ) → Sector → ℚ,
      IsComponentKBody 3 F ∧ ProjectedRestrictsTo 3 F zeroPaddedChart :=
  (fieldSpace_projected_atlas_gluing zeroPaddedChart).mp zeroPaddedChart_shared_compatible

/-- A concrete extension keeps the absent T equation unobserved, rather than
requiring it to be zero on charts that do not contain T. -/
def repairedExample (φ : Sector → ℚ) (s : Sector) : ℚ :=
  if s = Sector.T then φ Sector.F else 0

theorem repairedExample_restricts : ProjectedRestrictsTo 3 repairedExample zeroPaddedChart := by
  intro T _ φ s hs
  simp [repairedExample, zeroPaddedChart, hs]

/-- The repair is compatible with, and does not erase, the old negative result. -/
theorem repair_preserves_full_vector_obstruction :
    ProjectedRestrictsTo 3 repairedExample zeroPaddedChart ∧
      ¬ ∃ F : (Sector → ℚ) → Sector → ℚ, FieldSpace.RestrictsTo 3 F zeroPaddedChart :=
  ⟨repairedExample_restricts, zeroPaddedChart_no_full_extension⟩

/-- A term involving three sectors other than its equation label. -/
def hiddenTriplet (φ : Sector → ℚ) (s : Sector) : ℚ :=
  if s = Sector.T then φ Sector.F * φ Sector.W * φ Sector.I else 0

theorem hiddenTriplet_is_three_body : FieldSpace.IsKBody 3 hiddenTriplet := by
  let support : Finset Sector := {Sector.F, Sector.W, Sector.I}
  refine ⟨fun S φ => if S = support then hiddenTriplet φ else 0, ?_, ?_⟩
  · intro S φ
    by_cases hS : S = support
    · subst S
      simp only [ite_true]
      funext s
      simp [hiddenTriplet, restrict, support]
    · simp [hS]
  · intro φ
    have hc : support.card ≤ 3 := by decide
    simp [hc]

/-- No triplet containing T can contain all three inputs of the hidden term. -/
theorem hiddenTriplet_projected_zero :
    ProjectedRestrictsTo 3 hiddenTriplet (fun _ _ _ => 0) := by
  intro A hA φ s hs
  by_cases hsT : s = Sector.T
  · subst s
    by_cases hF : Sector.F ∈ A
    · by_cases hW : Sector.W ∈ A
      · by_cases hI : Sector.I ∈ A
        · have hsub : ({Sector.F, Sector.W, Sector.I, Sector.T} : Finset Sector) ⊆ A := by
            simp only [insert_subset_iff, singleton_subset_iff]
            exact ⟨hF, hW, hI, hs⟩
          have hc := card_le_card hsub
          norm_num [hA] at hc
        · simp [hiddenTriplet, restrict, hI]
      · simp [hiddenTriplet, restrict, hW]
    · simp [hiddenTriplet, restrict, hF]
  · simp [hiddenTriplet, hsT]

/-- Ordinary three-body dependence alone cannot justify projected uniqueness. -/
theorem ordinary_three_body_not_unique :
    ∃ F G : (Sector → ℚ) → Sector → ℚ,
      FieldSpace.IsKBody 3 F ∧ FieldSpace.IsKBody 3 G ∧
      ProjectedRestrictsTo 3 F (fun _ _ _ => 0) ∧
      ProjectedRestrictsTo 3 G (fun _ _ _ => 0) ∧ F ≠ G := by
  refine ⟨hiddenTriplet, fun _ _ => 0, hiddenTriplet_is_three_body, ?_,
    hiddenTriplet_projected_zero, ?_, ?_⟩
  · exact ⟨fun _ _ => 0, by simp [DependsOn], by simp⟩
  · intro _ _ _ _ _
    rfl
  · intro h
    have e := congrFun (congrFun h (fun _ => 1)) Sector.T
    norm_num [hiddenTriplet] at e

end EFMWPost156Audit.ProjectedGluing
