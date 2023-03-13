from flask import Flask, jsonify, request, abort
import sqlite3
import os

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Define a route that returns all the data as a JSON response
@app.route('/get_data', methods=['GET'])
def get_data():
    data_type=request.args.get('data_type')
    snippet = request.args.get('snippet')
    if data_type=='video_games':
        conn = sqlite3.connect('../data/nctk.db', check_same_thread=False)
        if snippet == 'true':
            cursor=conn.execute('SELECT * FROM video_games1 LIMIT 20')

        elif snippet=='false':
            cursor=conn.execute('SELECT * FROM video_games1')
        else:
            abort(404)
        data = cursor.fetchall()
    context = {
        "@context": {
            "@schema": "SQLite"
        },
        "@type": "video_games",
        "@list": []
    }
    for row in data:
        result = {
            "@id": row[0],
            "Title": row[1],
            "Features.Handheld?": row[2],
            "Features.Max Players": row[3],
            "Features.Multiplatform?": row[4],
            "Features.Online?": row[5],
            "Metadata.Genres": row[6],
            "Metadata.Licensed?": row[7],
            "Metadata.Publishers": row[8],
            "Metadata.Sequel?": row[9],
            "Metrics.Review Score": row[10],
            "Metrics.Sales": row[11],
            "Metrics.Used Price": row[12],
            "Release.Console": row[13],
            "Release.Rating": row[14],
            "Release.Re-release?": row[15],
            "Release.Year": row[16],
            "Length.All PlayStyles.Average": row[17],
            "Length.All PlayStyles.Leisure": row[18],
            "Length.All PlayStyles.Median": row[19],
            "Length.All PlayStyles.Polled": row[20],
            "Length.All PlayStyles.Rushed": row[21],
            "Length.Completionists.Average": row[22],
            "Length.Completionists.Leisure": row[23],
            "Length.Completionists.Median": row[24],
            "Length.Completionists.Polled": row[25],
            "Length.Completionists.Rushed": row[26],
            "Length.Main + Extras.Average": row[27],
            "Length.Main + Extras.Leisure": row[28],
            "Length.Main + Extras.Median": row[29],
            "Length.Main + Extras.Polled": row[30],
            "Length.Main + Extras.Rushed": row[31],
            "Length.Main Story.Average": row[32],
            "Length.Main Story.Leisure": row[33],
            "Length.Main Story.Median": row[34],
            "Length.Main Story.Polled": row[35],
            "Length.Main Story.Rushed": row[36]
        }
        context["@list"].append(result)
        conn.close()
    return jsonify(context)

if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')

