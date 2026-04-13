============
Installation
============


.. contents:: Table of Contents

Spinning Up requires Python 3.10+, Gymnasium, and OpenMPI.

Spinning Up is currently supported on Linux and macOS.

.. admonition:: You Should Know

    Many examples and benchmarks in Spinning Up refer to RL environments that use the `MuJoCo`_ physics engine. MuJoCo is now open source and bundled with Gymnasium. The `Classic Control`_ and `Box2d`_ environments in Gymnasium are also available and totally free to use.

.. _`Classic Control`: https://gymnasium.farama.org/environments/classic_control/
.. _`Box2d`: https://gymnasium.farama.org/environments/box2d/
.. _`MuJoCo`: https://gymnasium.farama.org/environments/mujoco/

Installing uv
==============

This project uses `uv`_ for fast, modern Python dependency management. Install it with:

.. parsed-literal::

    curl -LsSf https://astral.sh/uv/install.sh | sh

For other installation methods, see the `uv installation docs`_.

.. _`uv`: https://docs.astral.sh/uv/
.. _`uv installation docs`: https://docs.astral.sh/uv/getting-started/installation/


Installing OpenMPI
==================

Ubuntu 
------

.. parsed-literal::

    sudo apt-get update && sudo apt-get install libopenmpi-dev


Mac OS X
--------
Installation of system packages on Mac requires Homebrew_. With Homebrew installed, run the following:

.. parsed-literal::

    brew install open-mpi

.. _Homebrew: https://brew.sh

Installing Spinning Up
======================

.. parsed-literal::

    git clone https://github.com/openai/spinningup.git
    cd spinningup
    uv sync

.. admonition:: You Should Know

    Spinning Up installs `Gymnasium`_ with classic control and box2d environments by default. MuJoCo environments are also available through Gymnasium with no additional license required.

.. _`Gymnasium`: https://gymnasium.farama.org/

Check Your Install
==================

To see if you've successfully installed Spinning Up, try running PPO in the LunarLander-v2 environment with

.. parsed-literal::

    uv run python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999

This might run for around 10 minutes, and you can leave it going in the background while you continue reading through documentation. This won't train the agent to completion, but will run it for long enough that you can see *some* learning progress when the results come in.

After it finishes training, watch a video of the trained policy with

.. parsed-literal::

    uv run python -m spinup.run test_policy data/installtest/installtest_s0

And plot the results with

.. parsed-literal::

    uv run python -m spinup.run plot data/installtest/installtest_s0


Installing MuJoCo Environments (Optional)
==========================================

MuJoCo is now open source and bundled with Gymnasium. To use MuJoCo environments, simply install the mujoco extra:

.. parsed-literal::

    uv pip install gymnasium[mujoco]

Then check that things are working by running PPO in the Walker2d-v4 environment with

.. parsed-literal::

    uv run python -m spinup.run ppo --hid "[32,32]" --env Walker2d-v4 --exp_name mujocotest
