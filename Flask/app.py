from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    name = '이기준'
    lotto = [16, 18, 22, 43, 32, 11]

    def generate_lotto_numbers():
    # 1부터 45까지의 숫자 중에서 6개를 무작위로 선택
        lotto_numbers = random.sample(range(1, 46), 6)
        lotto_numbers.sort()  # 번호를 정렬하여 출력
        return lotto_numbers
    
    random_lotto = generate_lotto_numbers()

    from collections import Counter

    def count_common_elements(list1, list2):
        # Counter를 사용하여 각 리스트의 요소 개수를 세기
        counter1 = Counter(list1)
        counter2 = Counter(list2)

    # 두 리스트에서 공통된 요소의 개수 세기
        common_elements_count = sum((counter1 & counter2).values())

        return common_elements_count


    # 공통된 요소의 개수 출력
    result = count_common_elements(lotto, random_lotto)

    context = {
        "name": name,
        "lotto": lotto,
        "random_lotto":random_lotto,
        "result": result
    }

    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is Mypage!'

@app.route('/movie')
def movie():
    query = request.args.get('query')
    res = requests.get(f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}")
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
    print(movie_list)
    return render_template('movie.html', data=movie_list)

if __name__== '__main__':
    app.run(debug=True)