**Status:** Maintenance (expect bug fixes and minor updates)

Welcome to Spinning Up in Deep RL! 
==================================

This is an educational resource produced by OpenAI that makes it easier to learn about deep reinforcement learning (deep RL).

For the unfamiliar: [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) (RL) is a machine learning approach for teaching agents how to solve tasks by trial and error. Deep RL refers to the combination of RL with [deep learning](http://ufldl.stanford.edu/tutorial/).

This module contains a variety of helpful resources, including:

- a short [introduction](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) to RL terminology, kinds of algorithms, and basic theory,
- an [essay](https://spinningup.openai.com/en/latest/spinningup/spinningup.html) about how to grow into an RL research role,
- a [curated list](https://spinningup.openai.com/en/latest/spinningup/keypapers.html) of important papers organized by topic,
- a well-documented [code repo](https://github.com/openai/spinningup) of short, standalone implementations of key algorithms,
- and a few [exercises](https://spinningup.openai.com/en/latest/spinningup/exercises.html) to serve as warm-ups.

Get started at [spinningup.openai.com](https://spinningup.openai.com)!


Installation
------------

Spinning Up requires Python >=3.10 and uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Quick Install

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repo
git clone https://github.com/openai/spinningup.git
cd spinningup

# Install with uv
uv sync
```

### Installing with Extras

```bash
# Install with test dependencies
uv sync --extra test

# Install with documentation build dependencies
uv sync --extra docs
```

### Running Algorithms

```bash
# Run PPO on CartPole
uv run python -m spinup.run ppo --env CartPole-v1 --exp_name ppo_cartpole

# Plot results
uv run python -m spinup.run plot data/ppo_cartpole

# Watch trained policy
uv run python -m spinup.run test_policy data/ppo_cartpole/ppo_cartpole_s0
```

### Building Documentation

```bash
# Build English docs
uv run sphinx-build -b html docs/ docs/_build/html

# Build Traditional Chinese docs
uv run sphinx-build -b html -D language=zh_TW docs/ docs/_build/html/zh-TW
```


Changes from Upstream
---------------------

This fork modernizes the original OpenAI Spinning Up with:

- **Python 3.10+** compatibility (tested up to 3.13)
- **uv** for fast, modern dependency management (replaces `setup.py`)
- **Gymnasium** replaces the deprecated `gym` library
- **PyTorch 2.0+** (updated from 1.3.1)
- **GitHub Actions** CI/CD (replaces Travis CI)
- **GitHub Pages** documentation hosting (replaces Read the Docs)
- **Traditional Chinese (繁體中文)** documentation translation
- TF1 algorithms are preserved as legacy code (optional, not supported on Python 3.10+)


Citing Spinning Up
------------------

If you reference or use Spinning Up in your research, please cite:

```
@article{SpinningUp2018,
    author = {Achiam, Joshua},
    title = {{Spinning Up in Deep Reinforcement Learning}},
    year = {2018}
}
```
