import game_state
import settings

settings = settings.settings()
game = game_state.game_state()

game.bank.establish_bank(settings)

print(game.bank.ledger.ledger.head())
print(game.bank.balance_sheet.balance_sheet)