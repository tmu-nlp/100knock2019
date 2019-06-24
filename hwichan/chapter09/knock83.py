from collections import Counter
import pickle


def main():
    # Counter(): 引数にlistを指定することにより キーにlist要素、値にその要素の出現回数
    count_tc = Counter()
    count_t = Counter()
    count_c = Counter()

    tc_list = []
    t_list = []
    c_list = []
    with open('context.txt', 'r') as f:
        for n, line in enumerate(f, 1):  # n : 総出現回数
            tc = line.strip()
            if len(tc.split('\t')) < 2:  # たまに文脈語がない場合がある
                continue

            tc_list.append(tc)  # 単語と文脈語のペア（タブ区切り）
            t_list.append(tc.split('\t')[0])  # 単語
            c_list.append(tc.split('\t')[1])  # 文脈語

            # 一気に追加すると重くなるため1000000行ずつ追加
            if n % 1000000 == 0:
                print(f'{n}行')

                count_tc.update(tc_list)
                count_t.update(t_list)
                count_c.update(c_list)

                tc_list = []
                t_list = []
                c_list = []

        # あまりを追加
        count_tc.update(tc_list)
        count_t.update(t_list)
        count_c.update(c_list)

        print(f'N = {n}')

    with open('count_tc', 'wb') as tc_file, \
            open('count_t', 'wb') as t_file, \
            open('count_c', 'wb') as c_file:

        pickle.dump(count_tc, tc_file)
        pickle.dump(count_t, t_file)
        pickle.dump(count_c, c_file)


if __name__ == "__main__":
    main()

# N = 68070563

