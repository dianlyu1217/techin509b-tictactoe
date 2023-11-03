import logic
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./logs/output.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(filename)s- %(lineno)d  - %(message)s')
logger = logging.getLogger('tictactoc')

if __name__ == '__main__':
	logger.info('game start')
	board = logic.make_empty_board()
	turn = 'X'
	logic.show_board(board)
	while True:
		print('Next turn: ', turn)
		r, c = logic.receive_input(board, turn)
		board[r][c] = turn
		logic.show_board(board)
		turn = logic.change_turn(turn)
		if logic.judge_winner(board):
			logger.info('game finished')
			break
