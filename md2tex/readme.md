# md2tex
カレントのファイルでのみ実行可能  
下記環境構築されている前提  
https://qiita.com/yamatora/items/5947a190726311018f54  

## multicolpar.sty

対訳を利用する前に下記設定を行う

1. [https://ctan.org/pkg/multicolpar](https://ctan.org/pkg/multicolpar)から`multicolpar.sty`をDL
2. 適したディレクトリに配置(OS等によって異なる)

    下記ディレクトリで動作を確認

    ```
    C:\texlive\2023\texmf-dist\tex\latex\tools
    ```

3. `ls-R`を更新

    ```
    mktexlsr
    ```

### 参考

- [translate_sample.pdf](http://www.ic.daito.ac.jp/~mizutani/tex/doc/translate/translate_sample.pdf)