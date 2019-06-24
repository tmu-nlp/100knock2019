from scipy import io
import pickle


def main():
    x300 = io.loadmat('knock_x300')['x300']

    with open('./pickles/t_dict', 'rb') as f:
        t_dict = pickle.load(f)

    # United StatesがなかったのでUnited_States_of_America
    print(x300[t_dict["United_States_of_America"]])


if __name__ == "__main__":
    main()
