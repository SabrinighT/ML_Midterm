from gym.envs.registration import (
    registry,
    register,
    make,
    spec,
    load_env_plugins as _load_env_plugins,
)
register(
    id="gym_examples/GridWorld-v0",
    entry_point="gym_examples.envs:GridWorldEnv",
)
register(
    id="gym_examples/taxi-v2",
    entry_point="gym_examples.envs:TaxiEnv",
    reward_threshold=8,
    max_episode_steps=200,
)
