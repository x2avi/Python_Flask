from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pascal', methods=['POST'])
def pascal():
    n = int(request.args.get('n'))
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return jsonify(triangle)

if __name__ == '__main__':
    app.run()
