# IBM Cloud上でPython/Flaskを動かす際の最低限のセット

- qiita記事「[FlaskをIBM Cloud(PaaS)上で動かす時の注意点メモ](https://qiita.com/ishida330/items/6e4e363923344fe31b83)」のコードです
- 作成時点: 2018/01/14

## clone後の要変更点
- manifest.yml - (必須) アプリの名前をご自分の設定したものに
- runtime.txt - (オプション) Pythonのバージョン
- requrements.txt - (オプション) Flaskのバーション　+ 必要なら利用しているエクステンションを追加

