from utils.data_reader import QuestionHandler
from utils.gamestate_manager import GameStateManager

Questions = QuestionHandler('data/')

# print(Questions)

Game = GameStateManager(Questions)

Game.start_game()