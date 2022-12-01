# Copyright 2021 National Technology & Engineering Solutions of Sandia, LLC (NTESS).
# Under the terms of Contract DE-NA0003525 with NTESS,
# the U.S. Government retains certain rights in this software.
"""This example demonstrates how to compute the difficulty of a given SampleSet."""
from riid.data.labeling import BACKGROUND_LABEL
from riid.data.synthetic.static import StaticSynthesizer, get_dummy_sampleset

seeds_ss = get_dummy_sampleset(as_seeds=True)

# Separate foreground seeds from background seeds
seeds_labels = seeds_ss.get_labels()
fg_seeds_ss = seeds_ss[seeds_labels != BACKGROUND_LABEL]
bg_seeds_ss = seeds_ss[seeds_labels == BACKGROUND_LABEL]

static_syn = StaticSynthesizer(
    snr_function="uniform",
    samples_per_seed=500
)

_, _, easy_ss = static_syn.generate(fg_seeds_ss=fg_seeds_ss, bg_seeds_ss=bg_seeds_ss)
easy_score = easy_ss.difficulty_score()
print(f"Difficulty score for Uniform:           {easy_score:.5f}")

static_syn.snr_function = "log10"
_, _, medium_ss = static_syn.generate(fg_seeds_ss=fg_seeds_ss, bg_seeds_ss=bg_seeds_ss)
medium_score = medium_ss.difficulty_score()
print(f"Difficulty score for Log10:             {medium_score:.5f}")

static_syn.snr_function_args = (.00001, .1)
_, _, hard_ss = static_syn.generate(fg_seeds_ss=fg_seeds_ss, bg_seeds_ss=bg_seeds_ss)
hard_score = hard_ss.difficulty_score()
print(f"Difficulty score for Log10 Low Signal:  {hard_score:.5f}")
