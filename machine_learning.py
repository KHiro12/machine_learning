import glob
import os


def read_data(folder_path):
	csv_list = os.path.join(folder_path, "*csv")
	file_list = glob.glob(csv_list)
	train_list = []
	check_list = []
	split_no = int((len(file_list) / 2) + 0.5)

	if len(file_list) > 1 and split_no != len(file_list):
		train_list = file_list[:split_no]
		check_list = file_list[split_no:]

	return train_list, check_list


if __name__ == "__main__":
	folder_path = os.path.join(os.getcwd(), "data")
	
	if os.path.exists(folder_path):
		# データの読み込み
		train_list, check_list = read_data(folder_path)
		print(train_list)
		print(check_list)
