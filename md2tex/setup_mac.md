---
title: Setup pandoc on macbook
---

# Environment

|           |                                 |
| --------- | ------------------------------- |
| PC        | Macbook (Retina, 12-inch, 2017) |
| Processor | 1.2GHz dual core intel Core m3  |
| Memory    | 8GB                             |
| Graphics  | Intel HD Graphics 615 1636 MB   |
| OS        | macOS Monterey                  |


# pandoc

```
brew install pandoc
```

`Error: Invalid cask: ~~`といったエラーが大量に出る

下記を参考に

[https://www.mathkuro.com/mac/brew-cask-command-error/#toc2](https://www.mathkuro.com/mac/brew-cask-command-error/#toc2)

```
git -C /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core fetch --unshallow
brew install pandoc
```

# texlive

- [https://texwiki.texjp.org/?TeX%20Live%2FMac](https://texwiki.texjp.org/?TeX%20Live%2FMac)

1. DL `install-tl-unx.tar.gz` from mirror site

    ```
    curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
    ```

2. unzip & move

    ```
    tar xvf install-tl-unx.tar.gz
    cd install-tl-2*
    ```

3. install

    ```
    sudo ./install-tl -no-gui -repository http://mirror.ctan.org/systems/texlive/tlnet/
    ```

    Start text-mode installer and enter `I` to install

4. Add symboric link

    ```
    sudo /usr/local/texlive/2022/bin/universal-darwin/tlmgr path add
    ```
