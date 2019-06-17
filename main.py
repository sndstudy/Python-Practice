def test_string():

    # 文字列出力
    print('test_string1')

    # 複数行の出力(クォート3つで囲む)
    test_str = """
    test_string2
    test_string3
    """
    print(test_str)

    # 文字列結合
    test_str2 = 'P' + 'y' + 't' + 'h' + 'o' + 'n'
    print(test_str2)

    test_str3 = 'Python'
    test_str3 += 'Java'
    print(test_str3)

    # 指定回数の繰り返し
    test_str4 = 'Hoge' * 5
    print(test_str4)

    # 数値から文字列へ変換
    test_int = 100
    print(str(test_int) + '円')

    # 文字列の置換
    test_str5 = 'abcde'
    print(test_str5.replace('a', 'z'))

    # 文字列の分割(リストで返却される)
    test_str6 = 'ab-cd-ef'
    print(test_str6.split('-'))

    # 文字列の桁揃え
    test_str7 = '123'
    print(test_str7.rjust(5, 'X'))  # 指定した文字列で埋める
    print(test_str7.zfill(5))       # 0で埋める

    # 文字列の検索(Booleanで返却)
    test_str8 = 'abcdefg'

    # 先頭で検索
    print(test_str8.startswith('a'))
    print(test_str8.startswith('z'))

    # 指定した文字列が含まれているか
    print('c' in test_str8)
    print('z' in test_str8)

    # 大文字小文字変換
    test_str9 = 'aBcDe'
    print(test_str9.lower())
    print(test_str9.upper())

    # 文字列の除去(引数なしは空白を除去する)
    test_str10 = '   abccba   '
    print(test_str10.lstrip())  # 先頭から除去
    print(test_str10.rstrip())  # 末尾から除去

    test_str11 = 'abccba'
    print(test_str11.lstrip('a'))  # 先頭から除去
    print(test_str11.rstrip('a'))  # 末尾から除去

if __name__ == '__main__':
    print('main.py start')
    test_string()
