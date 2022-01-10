from agents.agent import Agent


class Grass(Agent):

    def __init__(self, x, y, regrowth_time, green, actions):
        super().__init__(x, y)
        self.regrowth_time = regrowth_time
        self.green = green
        self.time_to_grow = 0
        self.actions = actions

    def perceive(self, env):
        pass

    def action(self, env):
        for action in self.actions:
            action.act(self, env)
