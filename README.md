# GeijutudenPaintTool
芸術伝用のペイントを作成するツールです。

<h1>使用方法</h1>
<h2>【アートカミオン芸術伝　自作ペイント作成支援ツール】</h2>

・これはアートカミオン芸術伝で好きな画像をペイントにしたいときに使用できるツールです。<br>
・画像の情報を改造コードとして出力し、ゲーム内で有効化することで好きな画像をペイントにするという手法です。<br>

<h2>【注意！】</h2>
・自分のパソコンでしか動作確認していないため、他のパソコンで動作するかはわかりません。<br>
・エミュレータはDuckStationにて行いました。他のエミュレータでの動作確認はしていません。<br>
・このツールで生成したコードは非常に不安定です。実機での動作はほぼ不可能です。<br>
・ゲーム途中でチートを有効化できるエミュレータでないと動作は不可能だと思います。<br>
・画像ファイル名に日本語が入っているとエラーが発生するので、全部ローマ字にしてください。<br>
・このツールを使用して発生したいかなる損害の責任も負いません。<br>
・このツールの再配布を禁じます。<br>

<h2>【使い方】</h2>
１．Geijutuden_Paintフォルダ内にあるimagesフォルダを開きます。<br>
２．さらに８つのフォルダがありますが、トラックのサイズに応じて好きな画像をフォルダ内に入れます。フォルダの対応表は下記の通りです。<br>

	_4T_10T_BACK→4tトラック、10tトラックの後部
	_4T_SIDE    →4tトラックの横、上
	_10T_SIDE   →10tトラックの横、上
	_DUMP_BACK  →ダンプの後ろ
	_DUMP_SIDE  →ダンプの横
	_FLATED_BACK→平ボディーの後ろ
	_FLATED_SIDE→平ボディーの横
	_PROTECTER  →ダンプ、平ボディーのプロテクター

３．Geijutuden_Paintフォルダに戻り、Geijutuden_Paint.exeを起動します。<br>
４．output imagesに芸術伝で反映されるイメージが出力され、output txtsに画像情報の入った改造コードが出力されます。<br>
５．芸術伝を起動し、関口工芸に行って「自分で絵を描く」を選択します。（このときチートは無効にしておいてください）<br>
６．ペイント制作画面になったら、出力した改造コードを有効化します。ペイントの元に戻すボタンを２回押し、どれでもいいので、色の値を変更するボタンを１回押します。<br>
７．ペイント名を適当に付けて、セーブしたら完了です。チートを無効化にして、ゲームをリセットしてください。<br>
８．再び関口工芸に行き、「ペイントする」で自分のペイントが入っていれば成功です。<br>

このツールは３九の銀が作成しました。

<h1>Mac向けアプリケーションの作成（.appファイル化）について</h1>
すみませんが、私がMacを持っていないとappファイルの作成はできないようです。<br>
このプログラムはAnacondaによって作成されているので、各自でAnacondaをインストールして実行してください。<br>
https://www.google.com/search?q=anaconda+インストール+Mac <br>
また、opencvライブラリをAnacondaにインストールする必要があるため、コマンドラインで以下のコマンドを入力してください。<br>
	conda install opencv
