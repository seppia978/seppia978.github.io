---
title: 'When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models'

authors:
  - Sai Kartheek Reddy Kasu
  - Nils Lukas
  - admin

supervised_students:
  - Sai Kartheek Reddy Kasu

career_stage: postdoc

date: '2026-06-09T00:00:00Z'
doi: ''

publishDate: '2017-01-01T00:00:00Z'

publication_types: ['article']

publication: In *arXiv*
publication_short: In *arXiv*
abstract: |
  Failures in multi-turn reasoning models are largely invisible to terminal-score evaluation. A model can lock onto an unsafe stance early in a long dialogue, yet its final-turn refusal rate may appear indistinguishable from a robustly aligned baseline. To expose these hidden temporal dynamics, we propose a trace-level diagnostic: the CoT-Output 2x2 safety matrix. This framework labels every turn along two independent axes, internal reasoning and visible output, yielding four operationally defined failure cells: robust alignment, alignment faking, overt jailbreak, and context-injection failure. We evaluate three distilled reasoning targets against a fixed attacker across five oversight conditions, collecting 6750 turn-level observations on the Information-Hazard scenario. Our analysis reveals reproducible vulnerabilities in multi-turn safety evaluation, including an oversight paradox and context-injection failure.

summary: A trace-level diagnostic for safety failures that terminal refusal scores can miss in multi-turn reasoning models.

tags:
  - Chain-of-Thought
  - Multi-Turn Reasoning
  - AI Safety
  - Safety Evaluation

featured: false

url_pdf: 'https://arxiv.org/pdf/2606.10740'

image:
  caption: ''
  focal_point: ''
  preview_only: false
---
