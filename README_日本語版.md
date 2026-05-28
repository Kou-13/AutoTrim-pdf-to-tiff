# AutoTrim PDF to TIFF
PDFファイルの各ページを画像として読み込み、白い余白を自動でトリミングして、四角形のTIFF画像として保存するPythonスクリプトです。WindowsとmacOSの両方で使用できます。


◯機能
このスクリプトでは、以下の処理を行います。

1.PDFの各ページを画像として読み込みます。
2.白い余白を自動で検出し、四角形にトリミングしてTIFF形式で保存します。
3.PDFが複数ページある場合、各ページを連番のTIFF画像として保存します。
4.出力用フォルダは、入力PDFと同じ場所に自動で作成されます。


◯必要なライブラリ
必要なPythonライブラリは、requirements.txt に記載しています。
使用前に、requirements.txt に書かれているライブラリをインストールしてください。

通常は、以下のように実行します。
pip install -r requirements.txt

複数のPython環境を使っている場合は、このスクリプトを実行するPythonを指定してインストールしてください。
(Pythonのパス) -m pip install -r requirements.txt

現在使用しているPythonのパスは、Python上で以下を実行すると確認できます。
import sys
print(sys.executable)

※Python自体のインストール方法や、Spyderなどの開発環境の準備方法については、このREADMEでは説明しません。


◯使い方
AutoTrim_pdf_to_tiff.py を開き、上部にある「Settings」 セクションを書き換えてから実行してください。
主に変更する設定項目は、以下の4つです。

1.PDF_PATH
変換したいPDFファイルのパスを" "内に記入します。

重要：Path(r"...") の r を消さないでください。
rが記載されていることで、WindowsとmacOSの両方で使用可能です。
r を消すと、Windowsのパスに含まれる \ が正しく扱われず、エラーになる場合があります。

2.OUTPUT_FOLDER_NAME
出力画像を保存するフォルダ名を指定します。
このフォルダは、入力PDFと同じディレクトリに自動で作成されます。

3.TARGET_DPI
出力画像の解像度を指定します。
値が大きいほど高解像度になります。

通常は250-300ほどで使用し、高解像度が必要な場合に600を目安に変更してください。解像度が大きいほど画像サイズも大きくなりますのでご注意ください。

4.FILE_PREFIX
出力される画像ファイル名の先頭部分を指定します。
PDFが複数ページある場合、ページ順に連番で保存されます。

例：FILE_PREFIX = "Fig_" → Fig_1.tif、Fig_2.tif、Fig_3.tif


◯PDFの準備について
このスクリプトで解像度を指定しても、元のPDFが低解像度だと画像サイズが大きくなるだけで見た目に変化が無く、意味がありません。
そのため、PowerPointで作成した図表をPDF化する場合、PowerPointのエクスポート機能ではなく、印刷機能からPDFを作成することをおすすめします。
また、PowerPoint側の設定で、画像を圧縮しない設定や高解像度を保持する設定を行うと、より綺麗な画像を保存しやすくなります。


◯注意点
・同じ名前の出力ファイルが既に存在する場合、上書きされます。
・入力PDF自体は変更されません。
・WHITE_THRESHOLD は、白い余白を判定するための内部設定です。通常は変更しないでください。


◯トラブルシューティング
・PDFが見つからない場合
PDF_PATH が正しいか確認してください。特にWindowsでは、Path(r"...") の r を消さないでください。

・ライブラリが見つからない場合
以下のようなエラーが出る場合があります。

ModuleNotFoundError: No module named 'fitz'
ModuleNotFoundError: No module named 'PIL'

この場合、必要なライブラリが、実行中のPython環境にインストールされていません。
requirements.txt に書かれているライブラリをインストールしてください。

・出力画像が粗い場合
TARGET_DPI の値を大きくするか、PowerPoint側で高解像度に保持するよう設定するか、印刷からPDFを作成してください。

・余白のトリミングがうまくいかない場合
このスクリプトは、白い背景を余白として判定しています。
背景が完全な白ではない場合はコンテンツとして認識され、トリミングされません。


License

This project is released under the MIT License.
