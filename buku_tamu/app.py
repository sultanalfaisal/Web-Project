from flask import Flask, render_template, request

app = Flask(__name__)

semua_pesan = []

@app.route('/bukutamu', methods=['GET', 'POST'])
def buku_tamu():
    global semua_pesan

    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = request.form.get('pesan')
        data_baru = {'nama': nama, 'pesan': pesan}
        semua_pesan.append(data_baru)

    return render_template('bukutamu.html', semua_pesan=semua_pesan)

if __name__ == '__main__':
    app.run(debug=True)
    