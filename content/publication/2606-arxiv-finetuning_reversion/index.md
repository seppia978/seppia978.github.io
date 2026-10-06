---
title: 'A Gravitational Interpretation of Safety Reversion under Fine-Tuning'

authors:
  - admin
  - Nils Lukas

career_stage: postdoc

date: '2026-06-26T00:00:00Z'
doi: ''

publishDate: '2017-01-01T00:00:00Z'

publication_types: ['article']

publication: In *arXiv*
publication_short: In *arXiv*
abstract: |
  Safety alignment in large language models can degrade during post-training even when neither the data nor the objective is intentionally adversarial. Alignment rebound and reverse dynamics suggest that this degradation may reactivate behavior suppressed during safety alignment. Building on these ideas, we hypothesize that ordinary non-adversarial post-training follows a reversion direction: the activation-space displacement from the safety-aligned model toward a more permissive, earlier helpful-only state. We see that for Llama, every tested trajectory across references, tasks, and seeds exceeds a matched empirical null, while at aligned Llama and Qwen checkpoints, a vocabulary readout shows that the direction locally favors task-engaging over fixed refusal-like openings. Its geometric expression is behaviorally informative: as post-training proceeds, alignment with the direction and harmfulness increase together, yielding a strong descriptive correlation (Spearman r=0.958). To move beyond correlation, we test causal relevance during adaptation using objectives constructed from this coordinate. Across all tested Llama, Qwen, and Gemma settings from 3B to 14B, an optimizer-matched objective opposing positive motion reduces geometric alignment and harmfulness relative to ordinary fine-tuning, whereas a separately stabilized objective reinforcing that motion increases both. Every model and scale exhibits the same mean block-baseline-push ordering, showing that the causal relevance of the reversion direction is not tied to one architecture or model size. Finally, we show that a standard safety-rehearsal objective, built without access to the direction, independently opposes it and cuts cumulative reversion by about 30% in Llama and Qwen.

summary: Benign post-training pulls safety-aligned LLMs back along a reversion direction toward an earlier, more permissive state; opposing that direction reduces harmfulness across Llama, Qwen, and Gemma.

tags:
  - Fine-Tuning Reversion
  - Safety Reversion
  - AI Safety
  - Mechanistic Understanding
  - Model Adaptation

featured: true

url_pdf: 'https://arxiv.org/pdf/2606.28525'

image:
  caption: ''
  focal_point: ''
  preview_only: false
---
