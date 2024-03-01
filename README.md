# はじめに
このソフトウェアは、PNG、JPG、JPEGの画像を二値化し、標準偏差のスコアを計算するアプリケーションです。

# 使い方
1. アプリケーションを開きます。
2. メニューから「ファイル」→「開く」を選択します。
3. PNG、JPG、JPEGの画像ファイルを選択します。
4. アプリケーションは選択された画像を即座に二値化し、標準偏差のスコアを計算します。
5. 標準偏差が高いほど、画像のコントラストが高いことを示します。

# パッケージ
以下のファイルに、このアプリケーションで使用されるパッケージの一覧が記載されています。
- [installed_packages.md](./installed_packages.md)

# exe化の方法
このアプリケーションをexeファイルに変換する方法について説明します。

## pyinstallerでexe化
1. コマンドプロンプトやターミナルを開きます。
2. 以下のコマンドを入力して、PyInstallerをインストールします。

    ```
    pip install pyinstaller
    ```

3. PyInstallerが正常にインストールされたら、Pythonスクリプトをexeファイルに変換します。次のコマンドを使用します。

    ```
    pyinstaller --onefile your_script_name.py
    ```

    `your_script_name.py`はGUIアプリケーションのPythonスクリプトのファイル名に置き換えてください。

4. これにより、distディレクトリ内にexeファイルが生成されます。exeファイルを実行すると、アプリケーションが起動します。
