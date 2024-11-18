import string
from tabulate import tabulate
from termcolor import colored

ALPHABET = list(string.ascii_uppercase)
FREQUENCIES = {
    "E": 12.02,
    "T": 9.10,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.30,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.10,
    "Z": 0.07,
}
INPUT_STRING = """Ixkviatgl Udasxhtwxng Gn. 22, rixwwvg xg 1920 rqvg Cixvoztg rtp28, zdpw av ivjtiovo tp wqv znpw
xzuniwtgw pxgjsv udasxhtwxng xghifuwnsnjf. Xw wnnl wqv phxvghv xgwn t gvr rniso. Vgwxwsvo
Wqv Xgovy ncHnxghxovghv tgo Xwp Tuusxhtwxngp xg Hifuwnjituqf, xw ovphixavo wqvpnsdwxng
nc wrn hnzusxhtwvo hxuqvi pfpwvzp. Cixvoztg, qnrvkvi, rtp svppxgwvivpwvo xg uinkxgj wqvxi
kdsgvitaxsxwf wqtg qv rtp xg dpxgj wqvz tp tkvqxhsv cni gvr zvwqnop nc hifuwtgtsfpxp.Xg xw,
Cixvoztg ovkxpvo wrn gvr wvhqgxbdvp. Ngv rtp aixssxtgw. Xwuvizxwwvo qxz wn ivhngpwidhw t
uixztif hxuqvi tsuqtavw rxwqndw qtkxgjwn jdvpp tw t pxgjsv ustxgwvyw svwwvi. Adw wqv nwqvi
rtp uincndgo. Cni wqvcxipw wxzv xg hifuwnsnjf, Cixvoztg wivtwvo t civbdvghf oxpwixadwxng tp
tgvgwxwf, tp t hdikv rqnpv pvkvits unxgwp rviv htdptssf ivstwvo, gnw tp edpwt hnssvhwxng nc
xgoxkxodts svwwvip wqtw qtuuvg wn pwtgo xg t hviwtxg niovicni gnghtdpts (qxpwnixhts) ivtpngp,
tgo wn wqxp hdikv qv tuusxvo pwtwxpwxhtshnghvuwp. Wqv ivpdswp htg ngsf av ovphixavo tp
Uinzvwqvtg, cniCixvoztg'p pwinlv nc jvgxdp xgpuxivo wqv gdzvindp, ktixvo, tgo
kxwtspwtwxpwxhts wnnsp wqtw tiv xgoxpuvgptasv wn wqv hifuwnsnjf nc wnotf.Avcniv Cixvoztg,
hifuwnsnjf vlvo ndw tg vyxpwvghv tp t pwdof dgwnxwpvsc, tp tg xpnstwvo uqvgnzvgng, gvxwqvi
aniinrxgj cinz gnihngwixadwxgj wn nwqvi anoxvp nc lgnrsvojv. Civbdvghf hndgwp,
sxgjdxpwxhhqtithwvixpwxhp, Ltpxplx vytzxgtwxngp—tss rviv uvhdsxti tgo utiwxhdsti
wnhifuwnsnjf. Xw orvsw t ivhsdpv xg wqv rniso nc phxvghv. Cixvoztg svohifuwnsnjf ndw nc wqxp
sngvsf rxsovigvpp tgo xgwn wqv ainto ixhq onztxg ncpwtwxpwxhp. Qv hnggvhwvo hifuwnsnjf wn
ztwqvztwxhp. Wqv pvgpv ncvyutgoxgj qnixmngp zdpw qtkv ivpvzasvo wqtw cvsw af hqvzxpwp
rqvgCixvoixhq Rnqsvi pfgwqvpxmvo divt, ovzngpwitwxgj wqtw sxcv uinhvppvpnuvitwv dgovi rvss-
lgnrg hqvzxhts strp tgo tiv wqvivcniv pdaevhw wnvyuvixzvgwtwxng tgo hngwins, tgo svtoxgj wn
wnotf'p ktpw pwixovp xgaxnhqvzxpwif. Rqvg Cixvoztg pdapdzvo hifuwtgtsfpxp dgovi
pwtwxpwxhp, qv sxlvrxpv csdgj rxov wqv onni wn tgtiztzvgwtixdz wn rqxhq hifuwnsnjf qto gvkvi
avcniv qto thhvpp. Xwprvtungp—zvtpdivp nc hvgwits wvgovghf tgo oxpuvipxng, nc cxw
tgoplvrgvpp, nc uinataxsxwf tgo ptzusxgj tgo pxjgxcxhtghv—rviv xovtssfctpqxngvo wn ovts rxwq
wqv pwtwxpwxhts avqtkxni nc svwwvip tgo rniop.Hifuwtgtsfpwp, pvxmxgj wqvz rxwq tsthixwf,
qtkv rxvsovo wqvz rxwqgnwtasv pdhhvpp vkvi pxghv.Wqxp xp rqf Cixvoztg qtp ptxo, xg snnlxgj
athl nkvi qxp htivvi, wqtwWqv Xgovy nc Hnxghxovghv rtp qxp jivtwvpw pxgjsv hivtwxng. Xw tsngv
rndsoqtkv rng qxz qxp ivudwtwxng. Adw xg cthw xw rtp ngsf wqv avjxggxgj. Qv tgo Zip. Cixvoztg
bdxw Ixkviatgl gvti wqv vgo nc 1920. Wqvpxwdtwxng qto avhnzv xgwnsvitasv. Ctaftg qto sdivo qxz
athl tcwvi wqvrti rxwq itxpvp tgo uinzxpvp nc tapnsdwv civvonz wn uinkv ni oxpuinkvwqv
vyxpwvghv nc hxuqvip xg Pqtlvpuvtiv. Adw qv qto pbdvshqvo vkviftwwvzuw wn on pn tgo qto
vzatiitppvo Cixvoztg xgwn tuutivgwsfthbdxvphvgw pxsvghv tw stgwvig-psxov svhwdivp ng wqv
pdaevhw. Ng Etgdtif1, 1921, Cixvoztg avjtg t pxy-zngwq hngwithw rxwq wqv Pxjgts Hniup
wnovkxpv hifuwnpfpwvzp. Rqvg xw vyuxivo, qv rtp wtlvg ng wqv hxkxs-pvikxhvutfinss nc wqv Rti
Ovutiwzvgw tw $4,500 t fvti.Ngv nc qxp cxipw tppxjgzvgwp rtp wn wvthq t hndipv xg zxsxwtif
hnovptgo hxuqvip tw wqv Pxjgts Phqnns, wqvg tw Htzu Tscivo Ktxs, Gvr Evipvf.Cni wqxp qv rinwv
t wvywannl wqtw, cni wqv cxipw wxzv, xzunpvo niovi dungwqv hqtnp nc hxuqvi pfpwvzp tgo wqvxi
wvizxgnsnjf. Wqvpv qto puindwvoxg t avrxsovixgj ktixvwf, tgo rixwvip wivtwvo vthq tp xgoxkxodts
tgopuvhxts htpvp. Cixvoztg pniwvo wqvz ndw ng wqv atpxp nc pwidhwdivxgpwvto nc tpuvhw, tgo
pn snjxhts tgo dpvcds rtp wqxp hstppxcxhtwxng wqtw xwqtp avhnzv pwtgotio. Qv znovsvo qxp
gnzvghstwdiv ng qxp htwvjnixvp, pnwqtw wqv gtzvp qv zxgwvo qtkv wqv jivtw zvixw nc ztlxgj wqv
ivstwxngpavwrvvg wqv ktixndp jvgvit nc hxuqvip vkxovgw ng pxjqw. Tg vytzusv xp
wqvhnzusvzvgwtif utxi "zngn-tsuqtavw" tgo "unsftsuqtavw"; wqv Civghqrviv pwxss htssxgj
unsftsuqtavwxh pfpwvzp af wqv tsznpw nacdphtwnif"ondasv pdapwxwdwxng," rqxhq wvssp
tapnsdwvsf gnwqxgj tw tss tandw wqvpfpwvz. Cixvoztg'p znpw xzuniwtgw hnxgtjv rtp wqv
rnio"hifuwtgtsfpxp," rqxhq qv ovkxpvo xg 1920 wn hsvti du t hqingxh pndihv nchngcdpxng xg
hifuwnsnjf—wqv tzaxjdxwf nc wqv kvia "ovhxuqvi," wqvg dpvown zvtg anwq tdwqnixmvo tgo
dgtdwqnixmvo ivodhwxngp nc t hifuwnjitz wn ustxgwvyw.Qv wxwsvo qxp annl Vsvzvgwp nc
Hifuwtgtsfpxp, tgo wqv wviz qtp pnuinpuvivo wqtw wnotf xw hxihdstwvp xg jvgvits hngkviptwxng
tgo uixgw.
"""

cipher_key = {letter: None for letter in ALPHABET}
v1_cipher_key = {
    "V": "e",
    "T": "a",
    "W": "t",
    "Q": "h",
    "N": "o",
    "G": "n",
    "C": "f",
    "I": "r",
    "S": "l",
    "F": "y",
    "O": "d",
    "P": "s",
    "J": "g",
    "X": "i",
    "R": "w",
    "H": "c",
    "A": "b",
    "U": "p",
    "D": "u",
    "Z": "m",
    "L": "k",
    "K": "v",
    "Y": "x",
    "B": "q",
    "E": "j",
}


def calculate_frequencies(s):
    freq = {letter: 0 for letter in string.ascii_uppercase}

    for i in s.upper():
        if i in ALPHABET:
            freq[i] += 1

    return freq


def build_table(frequencies, title):
    sorted_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    table = [[letter, freq] for letter, freq in sorted_freq]
    return tabulate(table, headers=[title, "Frequency"], tablefmt="pretty").split("\n")


def side_by_side_tables(table1, table2):
    combined = []
    max_len = max(len(table1), len(table2))
    for i in range(max_len):
        line1 = table1[i] if i < len(table1) else " " * len(table1[0])
        line2 = table2[i] if i < len(table2) else " " * len(table2[0])
        combined.append(f"{line1}   {line2}")
    return "\n".join(combined)


def colorize_lowercase(text):
    colored_text = ""
    color = "green"
    for char in text:
        if char.islower():
            colored_text += colored(char, color)
        else:
            colored_text += char
    return colored_text


def update_cipher_key(sub, sub_with):
    v1_cipher_key[sub] = sub_with


def print_cipher_key():
    key_table = [
        [cipher_letter, cipher_key[cipher_letter] if cipher_key[cipher_letter] else "-"]
        for cipher_letter in ALPHABET
    ]
    print(
        tabulate(key_table, headers=["Cipher Letter", "Mapped To"], tablefmt="pretty")
    )


def apply_cipher_key():
    s_list = list(INPUT_STRING.upper())
    for i in range(len(s_list)):
        if s_list[i] in v1_cipher_key:
            update_cipher_key(s_list[i], v1_cipher_key[s_list[i]])
            s_list[i] = v1_cipher_key[s_list[i]]
    return "".join(s_list)


def substitute_letters(sub, sub_with, s):
    s_list = list(s)

    for i in range(len(s_list)):
        if s_list[i] == sub:
            s_list[i] = sub_with

    return "".join(s_list)


def main():
    message_frequencies = calculate_frequencies(INPUT_STRING)
    english_table = build_table(FREQUENCIES, "English Letter")
    message_table = build_table(message_frequencies, "Message Letter")
    tables = side_by_side_tables(english_table, message_table)
    s = INPUT_STRING.upper()

    print("Letter Frequency Comparison:\n")
    print(tables)
    print(f"\nInput string:\n\n{s}\n")
    while True:
        print("\nSelect an option:")
        print("1: Print frequencies")
        print("2: Print the key table")
        print("3: Decipher string")
        print("4 : Sub letters")
        print("e: Quit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "e":
            print("Exiting program.")
            break
        elif choice == "1":
            print("Letter Frequency Comparison:\n")
            print(tables)
        elif choice == "2":
            print("\nCurrent Cipher Key Table:\n")
            print_cipher_key()
        elif choice == "3":
            s = apply_cipher_key()
            print(f"\nDecrypted inputed string:\n\n{colorize_lowercase(s)}\n")

        elif choice == "4":
            a = input("Type the letter in the string to substitute: ").strip().upper()
            b = input("Type the letter to substitute with: ").strip().lower()
            s = substitute_letters(a, b, s)
            update_cipher_key(a, b)


if __name__ == "__main__":
    main()
