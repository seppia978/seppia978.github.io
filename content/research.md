---
title: 'Research'
date: 2026-07-01
type: landing

design:
  spacing: '5rem'

sections:
  - block: markdown
    id: compass
    content:
      title: Research Compass
      subtitle: ''
      text: |-
        <p class="research-lede">
          I study AI systems at the point where deployment changes them: fine-tuning, adaptation, misuse, new languages, new modalities, and new incentives.
        </p>

        <div class="research-manifesto">
          <p>
            My work is driven by a simple concern: alignment is not a one-time property. A model can look safe before release and become brittle after ordinary updates, downstream customization, or adversarial pressure. I am interested in the mechanisms behind that shift, and in evaluations that make those failures visible before they matter.
          </p>
          <p>
            I like research that connects control with understanding. Benchmarks are useful when they expose a real deployment failure mode; interpretability is useful when it changes what we can predict or prevent; defenses are useful when they survive contact with adaptation.
          </p>
        </div>
    design:
      columns: '1'
      css_class: research-focus-section research-manifesto-section
  - block: markdown
    id: principles
    content:
      title: What Guides Me
      subtitle: ''
      text: |-
        <ul class="research-principles-list">
          <li><strong>Safety must survive adaptation.</strong><span>Models are rarely frozen after release, so control mechanisms should be evaluated under benign and adversarial change.</span></li>
          <li><strong>Understanding should be actionable.</strong><span>Mechanistic insight matters most when it helps diagnose, predict, or intervene on model behavior.</span></li>
          <li><strong>Evidence beats surface behavior.</strong><span>Final answers, refusal rates, and aggregate scores can hide important failures; useful evaluations inspect traces, representations, and distributions.</span></li>
          <li><strong>Trustworthy AI is a systems problem.</strong><span>Safety, privacy, authenticity, and unlearning interact across training data, model internals, deployment interfaces, and human oversight.</span></li>
        </ul>
    design:
      columns: '1'
      css_class: research-principles-section
  - block: markdown
    id: threads
    content:
      title: Current Threads
      subtitle: ''
      text: |-
        <div class="research-focus-grid">
          <div class="research-focus-card">
            <h3>AI Control Across Deployment</h3>
            <p>Methods and evaluations for keeping language, vision-language, and generative models aligned before release and robust after fine-tuning, adaptation, or policy shifts.</p>
          </div>
          <div class="research-focus-card">
            <h3>The Mechanics of Model Change</h3>
            <p>Interpreting how fine-tuning changes models, from multilingual LLM safety to gravitational interpretations of fine-tuning reversion and future mechanistic studies.</p>
          </div>
          <div class="research-focus-card">
            <h3>Evidence, Forgetting & Forensics</h3>
            <p>Tools to explain decisions, remove learned information, and assess synthetic media, connecting XAI, unlearning, and deepfake robustness under one reliability lens.</p>
          </div>
        </div>

        <div class="research-quick-links">
          <a href="/#papers">Selected publications</a>
          <a href="/#news">Latest news</a>
          <a href="/#talks">Talks and lectures</a>
          <a href="mailto:s.poppi94@gmail.com">Start a conversation</a>
        </div>
    design:
      columns: '1'
      css_class: research-focus-section
---
