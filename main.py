from game import Game
from qgame import QGame
import pickle
from collections import defaultdict
 
if __name__ == "__main__":
    play_mode = input("Play mode? (play/qlearn):")
    if play_mode == "play":
        game = Game() # Play mode, uses game.py, defaults to random obstacles
    else:
        learn_mode = input("Learn mode? (fixed/random):")
        if learn_mode == "fixed":
            load_model = input("Load model? (y/n):")
            if load_model == "y":
                with open("q_table_fixed.pkl", "rb") as f:
                    q_table = pickle.load(f)
                print("Model loaded.")
                game = QGame(q_table = defaultdict(lambda: [0, 0], q_table), epsilon=0.05) # Loaded q_table, learn_mode = "fixed"
            else:
                game = QGame() # Default epsilon = 0.4, learn_mode = "fixed", default q_table
        else: 
            load_model = input("Load model? (y/n):")
            if load_model == "y":
                with open("q_table_random.pkl", "rb") as f:
                    q_table = pickle.load(f)
                print("Model loaded.")
                game = QGame(q_table = defaultdict(lambda: [0, 0], q_table), epsilon=0.05, learn_mode="random") # Loaded q_table, learn_mode = "random"
            else:
                game = QGame(learn_mode = "random") # Default epsilon = 0.4, learn_mode = "random", default q_table
        
    game.play()
    
    if play_mode == "play":
        exit()
    else: 
        save_model = input("Save model? (y/n):")
        if save_model == "y":
            if learn_mode == "fixed":
                with open("q_table_fixed.pkl", "wb") as f:
                    q_table_dict = dict(game.q_table)
                    pickle.dump(q_table_dict, f)
                print("Model saved.")
            else: 
                with open("q_table_random.pkl", "wb") as f:
                    q_table_dict = dict(game.q_table)
                    pickle.dump(q_table_dict, f)
                print("Model saved.")