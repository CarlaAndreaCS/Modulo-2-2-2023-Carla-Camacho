from app.components.game import Game

if __name__ == "__main__":
    game = Game()
    print("hello there...")
    while  game.game_running:
        if not game.playing:
            game.show_menu()