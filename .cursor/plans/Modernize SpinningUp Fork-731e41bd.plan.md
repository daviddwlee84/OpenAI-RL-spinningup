<!-- 731e41bd-1ac9-48d5-b6b8-43611d6efe5a -->
---
todos:
  - id: "pyproject"
    content: "Create pyproject.toml with modern deps (uv, Python 3.13, gymnasium, modern torch/sphinx)"
    status: pending
  - id: "update-algos"
    content: "Update PyTorch algorithm code: gym -> gymnasium API migration"
    status: pending
  - id: "update-tf1"
    content: "Handle TF1 code (drop/legacy-mark, pending user decision)"
    status: pending
  - id: "update-init"
    content: "Update spinup/__init__.py for new dependency structure"
    status: pending
  - id: "update-docs-conf"
    content: "Modernize docs/conf.py: myst-parser, i18n config, modern Sphinx APIs"
    status: pending
  - id: "gh-actions-ci"
    content: "Create .github/workflows/ci.yml for testing"
    status: pending
  - id: "gh-actions-docs"
    content: "Create .github/workflows/docs.yml for GitHub Pages deployment (en + zh-TW)"
    status: pending
  - id: "remove-travis"
    content: "Delete .travis.yml, travis_setup.sh, readthedocs.yml"
    status: pending
  - id: "i18n-setup"
    content: "Set up Sphinx i18n: generate .pot and .po files for zh-TW"
    status: pending
  - id: "translate-user"
    content: "Translate user docs (6 files): introduction, installation, algorithms, running, saving_and_loading, plotting"
    status: pending
  - id: "translate-rl-intro"
    content: "Translate RL intro docs (3 files): rl_intro, rl_intro2, rl_intro3"
    status: pending
  - id: "translate-resources"
    content: "Translate resources docs (4 files): spinningup, keypapers, exercises, bench"
    status: pending
  - id: "translate-algos"
    content: "Translate algorithm docs (6 files): vpg, trpo, ppo, ddpg, td3, sac"
    status: pending
  - id: "translate-utils-etc"
    content: "Translate utility + misc docs (7 files): logger, plotter, mpi, run_utils, acknowledgements, author, index"
    status: pending
  - id: "lang-switcher"
    content: "Add language switcher widget to Sphinx theme"
    status: pending
  - id: "update-readme"
    content: "Update readme.md with uv installation instructions"
    status: pending
  - id: "update-gitignore"
    content: "Update .gitignore for new build artifacts"
    status: pending
  - id: "cleanup"
    content: "Remove setup.py, docs_requirements.txt, verify build works"
    status: pending
isProject: false
---
# Modernize OpenAI Spinning Up Fork

## Overview

Three major modernization tasks: (1) migrate build/deps to uv + Python 3.13, (2) replace Travis CI with GitHub Actions for CI + GitHub Pages, (3) add Traditional Chinese documentation via Sphinx i18n with language switching.

---

## Task 1: Modernize Dependencies (uv + Python 3.13)

### 1a. Replace `setup.py` with `pyproject.toml`

- Create `pyproject.toml` at project root with `[build-system]` using `hatchling` or `setuptools`
- Move metadata from `setup.py` (name, version, description, dependencies)
- Add `[tool.uv]` section for uv-specific config
- Key dependency changes for Python 3.13 compatibility:
  - `gym~=0.15.3` -> `gymnasium` (modern replacement)
  - `torch==1.3.1` -> `torch>=2.0` (modern PyTorch)
  - `tensorflow>=1.8.0,<2.0` -> **drop or mark legacy** (TF1 is incompatible with Python 3.13; pending user decision)
  - `cloudpickle==1.2.1` -> unpin / use latest
  - `seaborn==0.8.1` -> unpin / use latest
  - `matplotlib==3.1.1` -> unpin / use latest
  - `recommonmark` (deprecated) -> `myst-parser` in docs deps
  - `sphinx==1.5.6` -> `sphinx>=7.0`
  - `sphinx-rtd-theme==0.4.1` -> `sphinx-rtd-theme>=2.0`
- Add `uv.lock` to `.gitignore` (or commit it, user preference)
- Remove old `setup.py` after migration

### 1b. Update algorithm code for modern deps

- Replace `import gym` with `import gymnasium as gym` across `spinup/algos/pytorch/`
- Update `gym.make()` calls for gymnasium API changes (e.g., `reset()` returns `(obs, info)`)
- Decision needed: TF1 algorithms -- drop, upgrade, or mark legacy
- Update `spinup/__init__.py` to conditionally import TF1 algos or remove them

### 1c. Update Sphinx docs config

- `docs/conf.py`: replace `recommonmark` with `myst-parser`, update `app.add_stylesheet` -> `app.add_css_file`, bump Sphinx config for modern version
- `docs/docs_requirements.txt` -> move doc deps into `pyproject.toml` under `[project.optional-dependencies.docs]`
- Update `docs/user/installation.rst` to document `uv`-based installation workflow

### 1d. Update README

- Update `readme.md` with new installation instructions using `uv`

---

## Task 2: Travis CI -> GitHub Actions

### 2a. Create CI workflow

- Create `.github/workflows/ci.yml`:
  - Trigger on push/PR to main/master
  - Set up Python 3.13 with `uv`
  - Install dependencies via `uv sync`
  - Run `python -c "import spinup"` smoke test
  - Run `pytest`

### 2b. Create GitHub Pages deployment workflow

- Create `.github/workflows/docs.yml`:
  - Trigger on push to main/master
  - Install doc dependencies via `uv sync --extra docs`
  - Build Sphinx docs: `sphinx-build docs/ docs/_build/html`
  - Build zh-TW docs: `sphinx-build -D language=zh_TW docs/ docs/_build/html/zh-TW`
  - Deploy to GitHub Pages using `actions/deploy-pages`
  - Add `.nojekyll` file for proper static serving

### 2c. Remove old CI files

- Delete `.travis.yml`
- Delete `travis_setup.sh`
- Delete `readthedocs.yml`

---

## Task 3: Traditional Chinese (zh-TW) Translation

### 3a. Set up Sphinx i18n infrastructure

- In `docs/conf.py`, add:
  - `locale_dirs = ['locales/']`
  - `gettext_compact = False`
- Add `sphinx-intl` to doc dependencies
- Generate `.pot` files: `sphinx-build -b gettext docs/ docs/_build/gettext`
- Generate zh-TW `.po` files: `sphinx-intl update -p docs/_build/gettext -l zh_TW`
- This creates `docs/locales/zh_TW/LC_MESSAGES/*.po` -- one `.po` per RST page

### 3b. Translate `.po` files (page-by-page)

Total: ~37 RST files, ~4474 lines. Key pages to translate:

- **User docs** (6 files): `introduction`, `installation`, `algorithms`, `running`, `saving_and_loading`, `plotting`
- **RL intro** (3 files): `rl_intro`, `rl_intro2`, `rl_intro3`
- **Resources** (4 files): `spinningup`, `keypapers`, `exercises`, `bench`
- **Algorithm docs** (6 files): `vpg`, `trpo`, `ppo`, `ddpg`, `td3`, `sac`
- **Utility docs** (4 files): `logger`, `plotter`, `mpi`, `run_utils`
- **Misc** (2 files): `acknowledgements`, `author`
- **Index**: `index`

Translation guidelines:
- Keep RL-specific terms in English with Chinese annotation on first occurrence, e.g., "強化學習 (Reinforcement Learning, RL)"
- Keep code snippets, API names, function names, class names untranslated
- Keep mathematical notation untranslated
- Section headers: translate but include English in parentheses for key terms

### 3c. Add language switcher

- Add a custom template `docs/_templates/versions.html` (or use `sphinx-rtd-theme`'s built-in version selector) to switch between `en` and `zh-TW`
- Alternatively, add a simple top-bar or sidebar widget linking `/` (English) and `/zh-TW/` (Chinese)
- The GitHub Pages workflow builds both language versions into separate subdirectories

### 3d. Directory structure after completion

```
docs/
  locales/
    zh_TW/
      LC_MESSAGES/
        index.po
        user/introduction.po
        user/installation.po
        ...
        spinningup/rl_intro.po
        ...
        algorithms/vpg.po
        ...
```

---

## File Change Summary

- **New files**: `pyproject.toml`, `.github/workflows/ci.yml`, `.github/workflows/docs.yml`, `docs/locales/zh_TW/LC_MESSAGES/*.po` (~37 files), `docs/_templates/languages.html`
- **Modified files**: `docs/conf.py`, `spinup/__init__.py`, `spinup/algos/pytorch/**/*.py` (gymnasium migration), `readme.md`, `.gitignore`
- **Deleted files**: `setup.py`, `.travis.yml`, `travis_setup.sh`, `readthedocs.yml`, `docs/docs_requirements.txt`
