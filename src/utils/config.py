from omegaconf import OmegaConf

conf = OmegaConf.load("../config.yaml")

conf.block = {}
conf.block.width = conf.window.width // conf.game.cols
conf.block.height = conf.window.height // conf.game.rows
