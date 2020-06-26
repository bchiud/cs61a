from __future__ import print_function
import code
import functools
import inspect
import re
import signal
import sys
import math
import sys
import numbers
import math
import numbers
import operator
import sys
import itertools
import string
import sys
import tokenize
'D9Ch3qW2n2_06_5_3__sq961_7'

def CK0_s(H_5yXx_):
    'F6W8T8f_O1954nfI81B0lUC16_'
    if (inspect.stack()[(((50 + -62) + (110 + -24)) + ((-218 + 79) + (72 + -6)))][0].f_locals[(chr((65 + 30)) + (('' + '_name') + ('_' + '_')))] == ((('' + '__m') + ('' + 'ai')) + ('' + ('n' + '__')))):
        pO4_15tm = sys.argv[(((218 + -100) + (-47 + 8)) + ((-71 + -50) + (65 + -22))):]
        H_5yXx_(*pO4_15tm)
    return H_5yXx_
V2F7 = str()

def W3o6(H_5yXx_):
    'Evz5Gsdk3wA72o1QM9D_w'

    @functools.wraps(H_5yXx_)
    def c3WB850_(*pO4_15tm, **X9Vq2):
        global V2F7
        ZZht_18__ = [repr(l0E808fa) for l0E808fa in pO4_15tm]
        ZZht_18__ += [((repr(u3dhwH3) + chr(((-40 + 60) + (141 + -100)))) + repr(fV_b8O_)) for (u3dhwH3, fV_b8O_) in X9Vq2.items()]
        A4Y7(((str() + (('{0' + '}(') + ('{' + '1})'))).format(H_5yXx_.__name__, (chr((74 + -30)) + chr(32)).join(ZZht_18__)) + chr(((108 + -24) + (46 + -72)))))
        V2F7 += ((chr(32) + ' ') + (' ' + chr(32)))
        try:
            kZ9O91gZy = H_5yXx_(*pO4_15tm, **X9Vq2)
            V2F7 = V2F7[:(- (((68 + 62) + (57 + -84)) + ((-159 + 42) + (-22 + 40))))]
        except Exception as l0E808fa:
            A4Y7((H_5yXx_.__name__ + (((' e' + 'xited via ex') + ('c' + 'ep')) + (('' + 'tio') + 'n'))))
            V2F7 = V2F7[:(- (((-4 + 21) + (-49 + -23)) + ((131 + -56) + (44 + -60))))]
            raise
        A4Y7(((chr(123) + ('0' + '}')) + (('({1}' + ') ->') + (' {2' + '}'))).format(H_5yXx_.__name__, (chr((-17 + 61)) + chr((-14 + 46))).join(ZZht_18__), kZ9O91gZy))
        return kZ9O91gZy
    return c3WB850_

def A4Y7(Ie59t6):
    'u730T29Z66_6_0Y_vo6l'
    print((V2F7 + re.sub(chr((-30 + 40)), (chr(((-94 + 96) + (27 + -19))) + V2F7), str(Ie59t6))))

def rt3__9():
    'IW6Mz8e_B86109488J60'
    k4101 = inspect.stack()[(((32 + -54) + (71 + 19)) + ((-121 + 5) + (-13 + 62)))]
    A4Y7(((('' + 'Curre') + ('nt l' + 'i')) + (('ne: File "{f[1]}", line {f[2' + ']}, in {f[3') + ('' + ']}'))).format(f=k4101))

def r0_1Ez_70(L23___=None):
    'I_84_3Iwi9kSj10_4w_t'
    k4101 = inspect.currentframe().f_back
    G9_9 = k4101.f_globals.copy()
    G9_9.update(k4101.f_locals)

    def h6MYP51Z_(signum, k4101):
        print()
        exit(int(((0.08689308363127402 + 0.3535267301936099) * int((0.39305408355656046 * 0)))))
    signal.signal(signal.SIGINT, h6MYP51Z_)
    if (not L23___):
        (k6o5, X_5c, V92r, k6o5, k6o5, k6o5) = inspect.stack()[(((-181 + 94) + (59 + 22)) + ((-138 + 64) + (121 + -40)))]
        L23___ = ((str() + ('Interacting at File "{0}' + '", l')) + ('i' + ('ne ' + '{1} \n'))).format(X_5c, V92r)
        L23___ += ((('  ' + '  Unix:    <Control>') + ('-D continues the ' + 'pro')) + (('g' + 'ram') + ('' + '; \n')))
        L23___ += ((('' + '  ') + ('  ' + 'W')) + (('indows: <Control>-Z <En' + 'ter> cont') + ('inues the program;' + ' \n')))
        L23___ += ((('' + '    ') + ('exit() o' + 'r')) + (('' + ' <Control>-C exits the') + (' p' + 'rogram')))
    code.interact(L23___, None, G9_9)
'NmM3pV_seF03_z2_26wM'
if (sys.version_info[int((((0.05650846494321038 + 0.3753912217896027) + (0.4023584487130063 + 0.0611676538541861)) * 0))] < (((40 + -9) + (-9 + 11)) + ((15 + 31) + (20 + -96)))):

    def input(z__f34):
        sys.stderr.write(z__f34)
        sys.stderr.flush()
        V92r = sys.stdin.readline()
        if (not V92r):
            raise EOFError()
        return V92r.rstrip((chr((16 + -3)) + chr((-64 + 74))))

class u9__(object):
    'J8_81pkm6_FCJd33M2HqNrjq74C'

    def __init__(z9ox6N_Q1, bYtOI):
        z9ox6N_Q1.index = 0
        z9ox6N_Q1.Ky5Q00 = []
        z9ox6N_Q1.bYtOI = bYtOI
        z9ox6N_Q1.current_line = ()
        z9ox6N_Q1.current()

    def JNZ6wu7_(z9ox6N_Q1):
        'V2prL7_Q_T6jo_Q1_oN36_wT5___5'
        current = z9ox6N_Q1.current()
        z9ox6N_Q1.index += (((-139 + 29) + (-73 + 84)) + ((176 + 0) + (-151 + 75)))
        return current

    def current(z9ox6N_Q1):
        'V98521811nLXe_3_ocBe4O'
        while (not z9ox6N_Q1.F49_454J):
            z9ox6N_Q1.index = int((((0.12221683613056566 + 0.010358681793518842) + (-0.2047329131452552 + 0.4699668927381422)) * int(((0.07201014930099991 + 0.5878502275972345) * int((0.9585284658206653 * 0))))))
            try:
                z9ox6N_Q1.current_line = next(z9ox6N_Q1.bYtOI)
                z9ox6N_Q1.Ky5Q00.append(z9ox6N_Q1.current_line)
            except StopIteration:
                z9ox6N_Q1.current_line = ()
                return None
        return z9ox6N_Q1.current_line[z9ox6N_Q1.index]

    @property
    def F49_454J(z9ox6N_Q1):
        return (z9ox6N_Q1.index < len(z9ox6N_Q1.current_line))

    def __str__(z9ox6N_Q1):
        'f21P2q6Jj_d3H9E2WIa_0U'
        mm88vm1__ = len(z9ox6N_Q1.Ky5Q00)
        L23___ = ((((('' + '{0') + chr(58)) + chr((156 + -94))) + str((math.floor(math.log10(mm88vm1__)) + (((-223 + 96) + (91 + -45)) + ((-24 + 58) + (116 + -68)))))) + (chr((202 + -77)) + (chr(58) + ' ')))
        Xd_f = str()
        for Y49w in range(max(int((0.15991649609101666 * 0)), (mm88vm1__ - (((26 + 31) + (-71 + 77)) + ((-55 + -62) + (83 + -25))))), (mm88vm1__ - (((-119 + 61) + (-40 + 87)) + ((41 + -19) + (19 + -29))))):
            Xd_f += ((L23___.format((Y49w + (((-48 + 27) + (-72 + 15)) + ((82 + -83) + (145 + -65))))) + chr((72 + -40)).join(map(str, z9ox6N_Q1.Ky5Q00[Y49w]))) + chr(((-29 + 35) + (81 + -77))))
        Xd_f += L23___.format(mm88vm1__)
        Xd_f += ' '.join(map(str, z9ox6N_Q1.current_line[:z9ox6N_Q1.index]))
        Xd_f += ('' + ((' ' + '>') + ('>' + ' ')))
        Xd_f += chr((79 + -47)).join(map(str, z9ox6N_Q1.current_line[z9ox6N_Q1.index:]))
        return Xd_f.strip()
try:
    import readline
except:
    pass

class YD8__E1Lt(object):
    'C91_y5_bm11_27vExcC9j13V7w2t'

    def __init__(z9ox6N_Q1, z__f34):
        z9ox6N_Q1.z__f34 = z__f34

    def __iter__(z9ox6N_Q1):
        while True:
            (yield input(z9ox6N_Q1.z__f34))
            z9ox6N_Q1.z__f34 = (' ' * len(z9ox6N_Q1.z__f34))

class r277_l55a(object):
    'Sjc0u_t578f1W2lJ6qT_6'

    def __init__(z9ox6N_Q1, Ky5Q00, z__f34, j12_S3=';'):
        z9ox6N_Q1.Ky5Q00 = Ky5Q00
        z9ox6N_Q1.z__f34 = z__f34
        z9ox6N_Q1.j12_S3 = j12_S3

    def __iter__(z9ox6N_Q1):
        while z9ox6N_Q1.Ky5Q00:
            V92r = z9ox6N_Q1.Ky5Q00.pop(int((0.2768901947888157 * 0))).strip(chr(((-134 + 99) + (104 + -59))))
            if ((z9ox6N_Q1.z__f34 is not None) and (V92r != str()) and (not V92r.lstrip().startswith(z9ox6N_Q1.j12_S3))):
                print((z9ox6N_Q1.z__f34 + V92r))
                z9ox6N_Q1.z__f34 = (' ' * len(z9ox6N_Q1.z__f34))
            (yield V92r)
        raise EOFError
'c_52_gNlqDB3D28rG9z_BFG'

class Pair(object):
    'F0krG_o6___6G29oe7x__'

    def __init__(z9ox6N_Q1, K60___u0, b21laz02):
        z9ox6N_Q1.K60___u0 = K60___u0
        z9ox6N_Q1.b21laz02 = b21laz02

    def __repr__(z9ox6N_Q1):
        return ((('Pair(' + '{0}') + (',' + ' ')) + (('{' + '1}') + ')')).format(repr(z9ox6N_Q1.K60___u0), repr(z9ox6N_Q1.b21laz02))

    def __str__(z9ox6N_Q1):
        Xd_f = (chr(((51 + 80) + (-51 + -40))) + repl_str(z9ox6N_Q1.K60___u0))
        b21laz02 = z9ox6N_Q1.b21laz02
        while isinstance(b21laz02, Pair):
            Xd_f += (chr((-56 + 88)) + repl_str(b21laz02.K60___u0))
            b21laz02 = b21laz02.b21laz02
        if (b21laz02 is not nil):
            Xd_f += ((str() + (chr(32) + ('.' + ' '))) + repl_str(b21laz02))
        return (Xd_f + chr(((92 + -69) + (-33 + 51))))

    def __len__(z9ox6N_Q1):
        (mm88vm1__, b21laz02) = ((((58 + -5) + (-38 + 43)) + ((-45 + 59) + (-82 + 11))), z9ox6N_Q1.b21laz02)
        while isinstance(b21laz02, Pair):
            mm88vm1__ += (((22 + 16) + (14 + 2)) + ((-34 + -39) + (118 + -98)))
            b21laz02 = b21laz02.b21laz02
        if (b21laz02 is not nil):
            raise TypeError((('' + ('len' + 'gth attem')) + (('pted on im' + 'pr') + ('op' + 'er list'))))
        return mm88vm1__

    def __eq__(z9ox6N_Q1, B9_hqRs):
        if (not isinstance(B9_hqRs, Pair)):
            return False
        return ((z9ox6N_Q1.K60___u0 == B9_hqRs.K60___u0) and (z9ox6N_Q1.b21laz02 == B9_hqRs.b21laz02))

    def map(z9ox6N_Q1, H_5yXx_):
        'UYI41_009G7i4919aAEn_Um0Q9'
        Mg412 = H_5yXx_(z9ox6N_Q1.K60___u0)
        if ((z9ox6N_Q1.b21laz02 is nil) or isinstance(z9ox6N_Q1.b21laz02, Pair)):
            return Pair(Mg412, z9ox6N_Q1.b21laz02.map(H_5yXx_))
        else:
            raise TypeError(((('il' + 'l') + ('-for' + 'm')) + (('' + 'ed') + (' ' + 'list'))))

class nil(object):
    'A9Ae9___7E324_359Iq0xIoTR11'

    def __repr__(z9ox6N_Q1):
        return ((chr(110) + 'i') + 'l')

    def __str__(z9ox6N_Q1):
        return (chr((-59 + 99)) + chr(41))

    def __len__(z9ox6N_Q1):
        return int((((-0.6681932014269942 + 0.5418483453601382) + (0.3635690640358692 + 0.2390736637390184)) * 0))

    def map(z9ox6N_Q1, H_5yXx_):
        return z9ox6N_Q1
nil = nil()
DPx0iP2 = {
    chr(39): ((str() + ('qu' + 'ot')) + chr(101)),
    chr(((40 + -9) + (32 + 33))): (('' + ('' + 'qu')) + (('asiq' + 'uot') + 'e')),
    (chr(44) + '@'): ((chr(117) + chr(110)) + (('quo' + 'te') + ('-' + 'splicing'))),
    chr((99 + -55)): (str() + (('' + 'un') + ('q' + 'uote'))),
}

def A1_Au9(Y__t):
    'S_UF69gQ_5Z9f9485J35A198qA6io'
    if (Y__t.current() is None):
        raise EOFError
    Z8HS3_ = Y__t.JNZ6wu7_()
    if (Z8HS3_ == ((chr(110) + 'i') + 'l')):
        return nil
    elif (Z8HS3_ == '('):
        return KA2R7_2(Y__t)
    elif (Z8HS3_ in DPx0iP2):
        return Pair(DPx0iP2[Z8HS3_], Pair(A1_Au9(Y__t), nil))
    elif (Z8HS3_ not in MCy826n):
        return Z8HS3_
    else:
        raise SyntaxError(((('une' + 'x') + ('' + 'pected tok')) + (('' + 'en: {') + ('' + '0}'))).format(Z8HS3_))

def KA2R7_2(Y__t):
    'd_2_e3vn1_2c15KHFraGZ411GK6Bm'
    try:
        if (Y__t.current() is None):
            raise SyntaxError(((('u' + 'nex') + ('' + 'pe')) + (('c' + 'te') + ('d end of f' + 'ile'))))
        elif (Y__t.current() == chr(41)):
            Y__t.JNZ6wu7_()
            return nil
        elif (Y__t.current() == chr((7 + 39))):
            Y__t.JNZ6wu7_()
            q1Gj04i = A1_Au9(Y__t)
            if (Y__t.current() is None):
                raise SyntaxError(((('unexpected' + ' en') + ('d' + ' ')) + (('' + 'of fi') + ('' + 'le'))))
            if (Y__t.JNZ6wu7_() != ')'):
                raise SyntaxError(((('expected one ' + 'elem') + ('e' + 'n')) + (('' + 't a') + ('' + 'fter .'))))
            return q1Gj04i
        else:
            K60___u0 = A1_Au9(Y__t)
            G_04 = KA2R7_2(Y__t)
            return Pair(K60___u0, G_04)
    except EOFError:
        raise SyntaxError(((('' + 'une') + ('x' + 'pected')) + ('' + (' end ' + 'of file'))))

def tjf7_65Al(z__f34='scm> '):
    'Jbm79u2_4h_OvB0685_h'
    return u9__(h8C4_wo(YD8__E1Lt(z__f34)))

def bNn5(Ky5Q00, z__f34='scm> ', ZBn5_k8=False):
    'wk8Pu_6B_J2_1VB64q698'
    if ZBn5_k8:
        J_sul8lp = Ky5Q00
    else:
        J_sul8lp = r277_l55a(Ky5Q00, z__f34)
    return u9__(h8C4_wo(J_sul8lp))

def yz43VA8(V92r):
    'L1019_6ERvIsY73nX04N_0__'
    return A1_Au9(u9__(h8C4_wo([V92r])))

def repl_str(Z8HS3_):
    'K2T_14382Th6k_46_19W14_44'
    if (Z8HS3_ is True):
        return (str() + ('' + ('' + '#t')))
    if (Z8HS3_ is False):
        return (chr(35) + chr(102))
    if (Z8HS3_ is None):
        return ((('u' + 'n') + ('d' + 'efi')) + ('' + ('ne' + 'd')))
    if (isinstance(Z8HS3_, numbers.Number) and (not isinstance(Z8HS3_, numbers.Integral))):
        return repr(Z8HS3_)
    return str(Z8HS3_)

def Z_Q59j():
    'ApqbC48089DC05____ab0H'
    while True:
        try:
            Y__t = tjf7_65Al((('r' + ('e' + 'a')) + (('' + 'd>') + ' ')))
            while Y__t.F49_454J:
                wR__ = A1_Au9(Y__t)
                print(((chr(115) + ('' + 'tr ')) + chr((-39 + 97))), wR__)
                print(((('' + 're') + 'p') + ('r' + ':')), repr(wR__))
        except (SyntaxError, ValueError) as r8882eH:
            print((type(r8882eH).__name__ + chr(((46 + -30) + (23 + 19)))), r8882eH)
        except (KeyboardInterrupt, EOFError):
            print()
            return

def CK0_s(*pO4_15tm):
    if (len(pO4_15tm) and ((chr(45) + (('-' + 'rep') + 'l')) in pO4_15tm)):
        Z_Q59j()
'v_580wV_PL9BG_25a76mO3_e62Wy'
try:
    import turtle
    import tkinter
except:
    print(((('warning: ' + 'could n') + ('ot ' + 'import the turtle modul')) + (chr(101) + '.')), file=sys.stderr)

class Bx_ERNR6(Exception):
    's__9D6_X9j5qqy473pS32rX724G0'
Y6__ = []

def S8yIW(*z_eUs):
    'l8kM9Tyco_84__Q83A9U_3rGi'

    def add(H_5yXx_):
        for C4ht_2N8 in z_eUs:
            Y6__.append((C4ht_2N8, H_5yXx_, z_eUs[0]))
        return H_5yXx_
    return add

def mM27GA4(Z8HS3_, F_4rA_7K, u3dhwH3, C4ht_2N8):
    'q0775m838_U16p_8c_b0WO72Au'
    if (not F_4rA_7K(Z8HS3_)):
        L23___ = ((chr(97) + ('rgument {0} of {1' + '} has wrong ty')) + (('pe' + ' ({') + ('2' + '})')))
        raise Bx_ERNR6(L23___.format(u3dhwH3, C4ht_2N8, type(Z8HS3_).__name__))
    return Z8HS3_

@S8yIW(((chr(98) + ('oolea' + 'n')) + chr((70 + -7))))
def Vg90x_(x4m63):
    return ((x4m63 is True) or (x4m63 is False))

def C_u1m_(Z8HS3_):
    'uJ3YXk5x82__659_Wr6w7_2vA_0'
    return (Z8HS3_ is not False)

def y02j4E(Z8HS3_):
    'p_64r961sjLLR5tN07j_r_Ry7XF6'
    return (Z8HS3_ is False)

@S8yIW((chr((149 + -39)) + ('' + ('' + 'ot'))))
def J_48(x4m63):
    return (not C_u1m_(x4m63))

@S8yIW((('e' + ('qua' + 'l')) + chr((-1 + 64))))
def a30_(x4m63, h02_D):
    if (hV8_81(x4m63) and hV8_81(h02_D)):
        return (a30_(x4m63.K60___u0, h02_D.K60___u0) and a30_(x4m63.b21laz02, h02_D.b21laz02))
    elif (l0Sf(x4m63) and l0Sf(h02_D)):
        return (x4m63 == h02_D)
    else:
        return ((type(x4m63) == type(h02_D)) and (x4m63 == h02_D))

@S8yIW((str() + ('' + ('eq' + '?'))))
def W68844GZ_(x4m63, h02_D):
    if (l0Sf(x4m63) and l0Sf(h02_D)):
        return (x4m63 == h02_D)
    elif (tHw1_52C4(x4m63) and tHw1_52C4(h02_D)):
        return (x4m63 == h02_D)
    else:
        return (x4m63 is h02_D)

@S8yIW(((str() + ('p' + 'a')) + (('' + 'ir') + chr(63))))
def hV8_81(x4m63):
    return isinstance(x4m63, Pair)

@S8yIW(((chr(112) + chr(114)) + (('o' + 'mis') + ('e' + '?'))))
def jLh9d_O(x4m63):
    return (type(x4m63).__name__ == ((chr(80) + chr(114)) + (('o' + 'mi') + ('' + 'se'))))

@S8yIW((chr(102) + ('o' + ('rc' + 'e'))))
def qR39(x4m63):
    mM27GA4(x4m63, jLh9d_O, int((0.06362270325463626 * 0)), ((str() + ('pr' + 'o')) + (str() + ('mi' + 'se'))))
    return x4m63.q_8_4()

@S8yIW(((str() + ('' + 'cdr-str')) + (('' + 'ea') + 'm')))
def kG_w__L(x4m63):
    mM27GA4(x4m63, (lambda x4m63: (hV8_81(x4m63) and jLh9d_O(x4m63.b21laz02))), int((((-0.7593598088945539 + 0.7685170045443321) + (-0.10979475948994455 + 0.8275298048799622)) * 0)), ((('' + 'cdr-') + 's') + (('' + 'tr') + ('ea' + 'm'))))
    return qR39(x4m63.b21laz02)

@S8yIW(((('n' + 'u') + chr(108)) + (chr(108) + chr(63))))
def P_0h_7(x4m63):
    return (x4m63 is nil)

@S8yIW((str() + (('lis' + 't') + '?')))
def eRY3S__9F(x4m63):
    'N1Rs96DMY_762F____o8wl_'
    while (x4m63 is not nil):
        if (not isinstance(x4m63, Pair)):
            return False
        x4m63 = x4m63.b21laz02
    return True

@S8yIW(((chr(108) + 'e') + (('n' + 'gt') + chr(104))))
def xPzt2(x4m63):
    mM27GA4(x4m63, eRY3S__9F, int(((-0.22107913296030468 + 0.9642724240186413) * int((0.5760886752222529 * 0)))), ((str() + ('l' + 'e')) + (('n' + 'g') + ('' + 'th'))))
    if (x4m63 is nil):
        return int((((-0.31919064700304545 + 0.7956626114649203) + (0.13803565821410457 + 0.11424298906467278)) * int(((-0.626133929775771 + 0.6608159272932634) * 0))))
    return len(x4m63)

@S8yIW((str() + (str() + ('co' + 'ns'))))
def g7_0_7c(x4m63, h02_D):
    return Pair(x4m63, h02_D)

@S8yIW((str() + ('' + ('c' + 'ar'))))
def tv_r46(x4m63):
    mM27GA4(x4m63, hV8_81, int((((-0.48986528002666707 + 0.4424338733428661) + (0.21248326611763957 + 0.12304020982963015)) * 0)), (str() + ('c' + ('' + 'ar'))))
    return x4m63.K60___u0

@S8yIW((str() + ('' + ('c' + 'dr'))))
def c8W68rQ1(x4m63):
    mM27GA4(x4m63, hV8_81, int((((-1.4900804848016447 + 0.970196002798017) + (0.4634471575954008 + 0.2600583709353612)) * 0)), (str() + (str() + ('cd' + 'r'))))
    return x4m63.b21laz02

@S8yIW((('' + ('' + 'se')) + (('t-' + 'car') + '!')))
def tv_r46(x4m63, h02_D):
    mM27GA4(x4m63, hV8_81, 0, (str() + (('' + 'set-car') + chr(33))))
    x4m63.K60___u0 = h02_D

@S8yIW(((chr(115) + ('et-' + 'cdr')) + chr((84 + -51))))
def c8W68rQ1(x4m63, h02_D):
    mM27GA4(x4m63, hV8_81, int(((0.7837154158465341 + 0.011354896961023653) * 0)), ((('se' + 't-c') + chr(100)) + (str() + ('' + 'r!'))))
    x4m63.b21laz02 = h02_D

@S8yIW((str() + (('l' + 'i') + ('s' + 't'))))
def u722nW_0(*uA_92):
    kZ9O91gZy = nil
    for l0E808fa in reversed(uA_92):
        kZ9O91gZy = Pair(l0E808fa, kZ9O91gZy)
    return kZ9O91gZy

@S8yIW((('' + ('ap' + 'p')) + ('e' + ('' + 'nd'))))
def j2_V6xZ_G(*uA_92):
    if (len(uA_92) == int((((-0.29215990691573335 + 0.5333535043944083) + (0.4185676024506265 + 0.32804090936328845)) * int(((0.41798562467825007 + 0.3272879627860332) * 0))))):
        return nil
    kZ9O91gZy = uA_92[(- (((145 + -8) + (-103 + 12)) + ((-11 + 36) + (-126 + 56))))]
    for Y49w in range((len(uA_92) - (((-51 + 29) + (95 + -42)) + ((23 + 33) + (-130 + 45)))), (- (((-195 + 58) + (158 + -74)) + ((86 + 25) + (-89 + 32)))), (- (((67 + -47) + (20 + -58)) + ((38 + 44) + (27 + -90))))):
        fV_b8O_ = uA_92[Y49w]
        if (fV_b8O_ is not nil):
            mM27GA4(fV_b8O_, hV8_81, Y49w, ((('' + 'ap') + ('' + 'pen')) + 'd'))
            S1_nmyE3_ = B9_hqRs = Pair(fV_b8O_.K60___u0, kZ9O91gZy)
            fV_b8O_ = fV_b8O_.b21laz02
            while hV8_81(fV_b8O_):
                B9_hqRs.b21laz02 = Pair(fV_b8O_.K60___u0, kZ9O91gZy)
                B9_hqRs = B9_hqRs.b21laz02
                fV_b8O_ = fV_b8O_.b21laz02
            kZ9O91gZy = S1_nmyE3_
    return kZ9O91gZy

@S8yIW(((('str' + 'i') + ('' + 'ng')) + chr(63)))
def AAia51(x4m63):
    return (isinstance(x4m63, str) and x4m63.startswith(chr(((-25 + -11) + (73 + -3)))))

@S8yIW((str() + (('' + 'symb') + ('o' + 'l?'))))
def tHw1_52C4(x4m63):
    return (isinstance(x4m63, str) and (not AAia51(x4m63)))

@S8yIW((('' + ('' + 'number')) + '?'))
def l0Sf(x4m63):
    return (isinstance(x4m63, numbers.Real) and (not Vg90x_(x4m63)))

@S8yIW(((('' + 'int') + ('e' + 'g')) + ('e' + ('r' + '?'))))
def XFqN_M7(x4m63):
    return (l0Sf(x4m63) and (isinstance(x4m63, numbers.Integral) or (int(x4m63) == x4m63)))

def d4mz222__(*uA_92):
    'nbwP__16_4278m_8_I9p_f0'
    for (Y49w, fV_b8O_) in enumerate(uA_92):
        if (not l0Sf(fV_b8O_)):
            L23___ = ((('o' + 'pera') + ('' + 'nd')) + (('' + ' {0} ({1}) is ') + ('not a' + ' number')))
            raise Bx_ERNR6(L23___.format(Y49w, fV_b8O_))

def v9l51(H_5yXx_, g_I6, uA_92):
    'iS2W7_1Uv_65ftT6661Lu810q_R4g'
    d4mz222__(*uA_92)
    Xd_f = g_I6
    for Z8HS3_ in uA_92:
        Xd_f = H_5yXx_(Xd_f, Z8HS3_)
    if (int(Xd_f) == Xd_f):
        Xd_f = int(Xd_f)
    return Xd_f

@S8yIW(chr((141 + -98)))
def x_2__08_(*uA_92):
    return v9l51(operator.add, int((((-1.5535914480164286 + 0.7120596195587108) + (0.7352013667340326 + 0.1918765089592943)) * 0)), uA_92)

@S8yIW(chr(((89 + 49) + (-88 + -5))))
def M4N_(j6Kg2, *uA_92):
    d4mz222__(j6Kg2, *uA_92)
    if (len(uA_92) == int((((-1.3914487429111728 + 0.9438037768535829) + (0.5496964226395028 + 0.18735592112933208)) * int(((-0.40022208084334776 + 0.6277844982867948) * int((0.44419589767375445 * 0))))))):
        return (- j6Kg2)
    return v9l51(operator.sub, j6Kg2, uA_92)

@S8yIW(chr(((174 + -39) + (-184 + 91))))
def qT63203(*uA_92):
    return v9l51(operator.mul, (((22 + 39) + (-148 + 90)) + ((-1 + -98) + (5 + 92))), uA_92)

@S8yIW(chr(((133 + -53) + (-86 + 53))))
def nY9HrRo23(j6Kg2, *uA_92):
    d4mz222__(j6Kg2, *uA_92)
    try:
        if (len(uA_92) == int((((0.12283526560559521 + 0.5013960128659914) + (0.07046186784064312 + 0.0036541175649054125)) * 0))):
            return operator.truediv((((193 + -59) + (-124 + 53)) + ((-211 + 82) + (100 + -33))), j6Kg2)
        return v9l51(operator.truediv, j6Kg2, uA_92)
    except ZeroDivisionError as r8882eH:
        raise Bx_ERNR6(r8882eH)

@S8yIW(((('' + 'ex') + 'p') + chr(116)))
def U8_R(j6Kg2, v_7_7xG__):
    d4mz222__(j6Kg2, v_7_7xG__)
    return pow(j6Kg2, v_7_7xG__)

@S8yIW((('' + ('' + 'ab')) + 's'))
def lV_L1(j6Kg2):
    return abs(j6Kg2)

@S8yIW(((('qu' + 'o') + ('t' + 'ie')) + ('' + ('n' + 't'))))
def D577I_B9k(j6Kg2, v_7_7xG__):
    d4mz222__(j6Kg2, v_7_7xG__)
    try:
        return ((- ((- j6Kg2) // v_7_7xG__)) if ((j6Kg2 < int((((-1.7803028923380784 + 0.9892783003153368) + (0.7469285645273258 + 0.06047272969039219)) * 0))) ^ (v_7_7xG__ < int(((-0.4380691351206497 + 0.46463464080368744) * int((0.7200766253718525 * 0)))))) else (j6Kg2 // v_7_7xG__))
    except ZeroDivisionError as r8882eH:
        raise Bx_ERNR6(r8882eH)

@S8yIW((('m' + chr(111)) + ('' + ('dul' + 'o'))))
def yur93Af(j6Kg2, v_7_7xG__):
    d4mz222__(j6Kg2, v_7_7xG__)
    try:
        return (j6Kg2 % v_7_7xG__)
    except ZeroDivisionError as r8882eH:
        raise Bx_ERNR6(r8882eH)

@S8yIW((chr((118 + -4)) + (('emai' + 'nd') + ('' + 'er'))))
def eb_D8674(j6Kg2, v_7_7xG__):
    d4mz222__(j6Kg2, v_7_7xG__)
    try:
        kZ9O91gZy = (j6Kg2 % v_7_7xG__)
    except ZeroDivisionError as r8882eH:
        raise Bx_ERNR6(r8882eH)
    while (((kZ9O91gZy < 0) and (j6Kg2 > int((((-0.8016350225021475 + 0.5030518009996168) + (0.34862369028748164 + 0.15706318858989732)) * int(((-0.13509092563473724 + 0.5076866789116444) * 0)))))) or ((kZ9O91gZy > int((((-0.7279831097436035 + 0.7528177787850443) + (0.9312038603765908 + 0.02183633333453805)) * int(((-0.2733001296146633 + 0.4648583518900037) * 0))))) and (j6Kg2 < int((((-0.4687036223944604 + 0.8852453985317954) + (-0.4373636226728346 + 0.8232232941958616)) * int(((0.26362173751260654 + 0.25350475383156434) * int((0.07264710657550089 * 0))))))))):
        kZ9O91gZy -= v_7_7xG__
    return kZ9O91gZy

def H3_1M4_(TL_3_y8Q6, C4ht_2N8, l_cRQ=None):
    'X7__AIB_aO_7N7_9761a'
    q94Q4_2i = (getattr(TL_3_y8Q6, C4ht_2N8) if (l_cRQ is None) else getattr(TL_3_y8Q6, C4ht_2N8, l_cRQ))

    def R942cA_S_(*uA_92):
        d4mz222__(*uA_92)
        return q94Q4_2i(*uA_92)
    return R942cA_S_
for MMs0it63k in [(str() + ('a' + ('' + 'cos'))), (chr(97) + ('c' + ('' + 'osh'))), ((str() + ('a' + 's')) + ('' + ('' + 'in'))), (chr((83 + 14)) + (('si' + 'n') + chr(104))), (('' + ('' + 'ata')) + chr((40 + 70))), (str() + (chr(97) + ('' + 'tan2'))), ((str() + ('a' + 't')) + (('' + 'an') + chr(104))), (str() + (('c' + 'e') + ('i' + 'l'))), (('c' + ('op' + 'ys')) + ('i' + ('' + 'gn'))), (str() + (chr(99) + ('' + 'os'))), ((str() + ('' + 'co')) + (chr(115) + chr(104))), (('' + ('d' + 'eg')) + (str() + ('re' + 'es'))), (chr(102) + (chr(108) + ('oo' + 'r'))), (str() + (('' + 'lo') + 'g')), (chr((120 + -12)) + (str() + ('o' + 'g10'))), (('' + ('lo' + 'g')) + (chr(49) + chr(112))), ((str() + ('rad' + 'i')) + (('' + 'an') + 's')), ('s' + (str() + ('' + 'in'))), (chr(115) + ('' + ('i' + 'nh'))), (chr((154 + -39)) + (('q' + 'r') + 't')), ((chr(116) + 'a') + chr(110)), (str() + (str() + ('tan' + 'h'))), ((('t' + 'r') + chr(117)) + (chr(110) + chr(99)))]:
    S8yIW(MMs0it63k)(H3_1M4_(math, MMs0it63k))
S8yIW(((('l' + 'o') + 'g') + chr((123 + -73))))(H3_1M4_(math, ('' + (('lo' + 'g') + chr(50))), (lambda x4m63: math.log(x4m63, (((-141 + 80) + (43 + -62)) + ((21 + -38) + (85 + 14)))))))

def S82T(i0T1En644, x4m63, h02_D):
    d4mz222__(x4m63, h02_D)
    return i0T1En644(x4m63, h02_D)

@S8yIW(chr(((185 + -68) + (-30 + -26))))
def MdeM(x4m63, h02_D):
    return S82T(operator.eq, x4m63, h02_D)

@S8yIW(chr(((-8 + 62) + (-11 + 17))))
def k49734y_(x4m63, h02_D):
    return S82T(operator.lt, x4m63, h02_D)

@S8yIW(chr(((23 + 35) + (-79 + 83))))
def N_ASe68L5(x4m63, h02_D):
    return S82T(operator.gt, x4m63, h02_D)

@S8yIW((str() + (str() + ('' + '<='))))
def a__e_(x4m63, h02_D):
    return S82T(operator.le, x4m63, h02_D)

@S8yIW((chr((63 + -1)) + chr((83 + -22))))
def b102wyES4(x4m63, h02_D):
    return S82T(operator.ge, x4m63, h02_D)

@S8yIW(((chr(101) + ('' + 'ven')) + chr(63)))
def i2_W_Em(x4m63):
    d4mz222__(x4m63)
    return ((x4m63 % (((-176 + 75) + (102 + -29)) + ((77 + -78) + (35 + -4)))) == 0)

@S8yIW(('' + (('' + 'odd') + chr(63))))
def d_h2(x4m63):
    d4mz222__(x4m63)
    return ((x4m63 % (((57 + 42) + (69 + -87)) + ((-178 + 69) + (0 + 30)))) == (((20 + -99) + (-25 + 78)) + ((166 + -88) + (-112 + 61))))

@S8yIW(((chr(122) + chr(101)) + (('' + 'ro') + chr(63))))
def J8446(x4m63):
    d4mz222__(x4m63)
    return (x4m63 == int((((-0.36172859891615594 + 0.672647849615356) + (-0.037871505005057204 + 0.24242272530292697)) * 0)))

@S8yIW(((('at' + 'o') + chr(109)) + '?'))
def b_fb7(x4m63):
    return (Vg90x_(x4m63) or l0Sf(x4m63) or tHw1_52C4(x4m63) or P_0h_7(x4m63) or AAia51(x4m63))

@S8yIW(('' + (chr(100) + ('ispl' + 'ay'))))
def AiN_x(Z8HS3_):
    if AAia51(Z8HS3_):
        Z8HS3_ = eval(Z8HS3_)
    print(repl_str(Z8HS3_), end=str())

@S8yIW(('p' + (('' + 'rin') + chr(116))))
def e4W5_t2_3(Z8HS3_):
    print(repl_str(Z8HS3_))

@S8yIW(((('' + 'ne') + ('w' + 'l')) + ('' + ('in' + 'e'))))
def GB__5():
    print()
    sys.stdout.flush()

@S8yIW(((('' + 'err') + chr(111)) + chr((30 + 84))))
def Y19ey90M1(L23___=None):
    L23___ = (str() if (L23___ is None) else repl_str(L23___))
    raise Bx_ERNR6(L23___)

@S8yIW(((chr(101) + 'x') + (str() + ('i' + 't'))))
def ANq0():
    raise EOFError
JI_rY = False
zc7Fu_3hy = True

def P__O():
    return JI_rY

def J8P_():
    global JI_rY
    if (not JI_rY):
        JI_rY = True
        turtle.title(('S' + (('c' + 'h') + ('eme' + ' Turtles'))))
        turtle.mode((('l' + 'o') + (str() + ('' + 'go'))))

@S8yIW(((chr(102) + ('' + 'or')) + ('w' + ('a' + 'rd'))), (str() + (chr(102) + chr(100))))
def g9_vX29_(mm88vm1__):
    's75_T7_Uv93_7XF0_0966l6'
    d4mz222__(mm88vm1__)
    J8P_()
    turtle.forward(mm88vm1__)

@S8yIW((str() + (str() + ('b' + 'ackward'))), ('b' + ('' + ('ac' + 'k'))), (chr(98) + 'k'))
def U0Cv878(mm88vm1__):
    'nn_Y_52EEs__ixz1Y_PD249_'
    d4mz222__(mm88vm1__)
    J8P_()
    turtle.backward(mm88vm1__)

@S8yIW(('' + (str() + ('lef' + 't'))), (str() + ('l' + chr(116))))
def qL046(mm88vm1__):
    'T6PH_i1_JU_e1_9_8f8R2_'
    d4mz222__(mm88vm1__)
    J8P_()
    turtle.left(mm88vm1__)

@S8yIW((('' + ('' + 'ri')) + (chr(103) + ('' + 'ht'))), (str() + (chr(114) + chr(116))))
def Y00w80(mm88vm1__):
    'fV3aBBD38_fHf_67k36Y51avnx_2'
    d4mz222__(mm88vm1__)
    J8P_()
    turtle.right(mm88vm1__)

@S8yIW(((str() + ('ci' + 'r')) + (('c' + 'l') + chr(101))))
def p6VsE244(S1_nmyE3_, t_lc__69n=None):
    'T_R13J1318_2_4wUJ_1c1_'
    if (t_lc__69n is None):
        d4mz222__(S1_nmyE3_)
    else:
        d4mz222__(S1_nmyE3_, t_lc__69n)
    J8P_()
    turtle.circle(S1_nmyE3_, (t_lc__69n and t_lc__69n))

@S8yIW(((('set' + 'posi') + chr(116)) + (str() + ('' + 'ion'))), (('' + ('' + 'se')) + (('t' + 'p') + ('' + 'os'))), (str() + (chr(103) + ('ot' + 'o'))))
def Nw_I2FF9(x4m63, h02_D):
    'DyF69_J23FCgOx3y00451E_N82'
    d4mz222__(x4m63, h02_D)
    J8P_()
    turtle.setposition(x4m63, h02_D)

@S8yIW(((str() + ('se' + 'th')) + (('e' + 'a') + ('din' + 'g'))), ('s' + (chr(101) + ('' + 'th'))))
def t_521_V(Ny0F42c):
    'kABGoCD3x_43y2__p8j8'
    d4mz222__(Ny0F42c)
    J8P_()
    turtle.setheading(Ny0F42c)

@S8yIW((str() + ('' + ('pen' + 'up'))), (str() + ('p' + chr(117))))
def P06LT5():
    'oEN_7oHyln_5keD1YV_6A02'
    J8P_()
    turtle.penup()

@S8yIW(((str() + ('pe' + 'n')) + (('' + 'do') + ('' + 'wn'))), ('p' + 'd'))
def BBASg2():
    'Cj__1Ab8T7Ftl02i_dZWzn3s5E23'
    J8P_()
    turtle.pendown()

@S8yIW(((('' + 'sho') + ('w' + 't')) + ('u' + ('rtl' + 'e'))), ('s' + chr((97 + 19))))
def e3Qjh_R_F():
    'k81W8Qp1___5Ia7UPHV116o31z609'
    J8P_()
    turtle.showturtle()

@S8yIW(((('' + 'hid') + 'e') + (('' + 'tu') + ('rtl' + 'e'))), (str() + (chr(104) + chr(116))))
def oM291():
    'Y47b___15Gx_4x1_258_p80Nw'
    J8P_()
    turtle.hideturtle()

@S8yIW((chr((153 + -54)) + (str() + ('l' + 'ear'))))
def n36f():
    'W86_6x0qi7_2qH8fL4_0Wwx'
    J8P_()
    turtle.clear()

@S8yIW((str() + (chr(99) + ('ol' + 'or'))))
def jtE9qdy(i1gB5):
    'gvD8674_RbkHhtsk79UM51Ob'
    J8P_()
    mM27GA4(i1gB5, AAia51, int(((0.3827478005741658 + 0.2760011039299134) * 0)), (chr((102 + -3)) + (str() + ('o' + 'lor'))))
    turtle.color(eval(i1gB5))

@S8yIW((str() + (('' + 'rg') + 'b')))
def K1Z_(QAD_, KqW_zd28, C074_):
    'px_gx___cw7Z7DeMNv1cZ_591Zr'
    JgWy = (QAD_, KqW_zd28, C074_)
    for x4m63 in JgWy:
        if ((x4m63 < int((((-0.7120007527974647 + 0.2554906835936156) + (0.8587543905198389 + 0.04090201413014327)) * int(((0.9134731279458057 + 0.036479182786755215) * 0))))) or (x4m63 > (((107 + -73) + (-55 + -37)) + ((44 + 1) + (42 + -28))))):
            raise Bx_ERNR6((((('Ill' + 'egal co') + ('lo' + 'r ')) + (('' + 'intens') + ('' + 'ity in '))) + repl_str(JgWy)))
    h_01p6 = tuple((int((x4m63 * (((139 + 82) + (-103 + 71)) + ((71 + 91) + (-191 + 95))))) for x4m63 in JgWy))
    return (((('' + '"#') + ('%02x' + '%')) + (('0' + '2x%') + ('0' + '2x"'))) % h_01p6)

@S8yIW((('b' + chr(101)) + (chr(103) + ('' + 'in_fill'))))
def b07Pg5ogg():
    'v_5_7j3_YA24813J__7yy36_'
    J8P_()
    turtle.begin_fill()

@S8yIW(((('e' + 'nd') + ('_' + 'fi')) + ('' + ('l' + 'l'))))
def M2i11500():
    'Lz74j5A9xX69B43R56l4j3o_09'
    J8P_()
    turtle.end_fill()

@S8yIW((('' + ('b' + 'gco')) + (('' + 'lo') + chr(114))))
def t_DD14(i1gB5):
    J8P_()
    mM27GA4(i1gB5, AAia51, int((((0.6093315594617381 + 0.06040556994623281) + (-0.58004490005454 + 0.8164444304469789)) * 0)), (('b' + ('gco' + 'l')) + (chr(111) + chr(114))))
    turtle.bgcolor(eval(i1gB5))

@S8yIW((('' + ('ex' + 'i')) + (('toncl' + 'ic') + chr(107))))
def G2w38w_P5():
    'Rj5rxLJs__18m_6j7Z6__32Xbq'
    global JI_rY
    if (zc7Fu_3hy and JI_rY):
        print(((('C' + 'lose') + (' or cl' + 'i')) + (('' + 'ck') + (' on turtle windo' + 'w to complete exit'))))
        turtle.exitonclick()
        JI_rY = False

@S8yIW(('s' + (('pe' + 'e') + chr(100))))
def B08J(Xd_f):
    'xekjP6Rlm3_yLSy5L6W31K3'
    mM27GA4(Xd_f, XFqN_M7, int(((-0.28005063664183616 + 0.5687972780894819) * 0)), (('' + ('sp' + 'ee')) + chr(100)))
    J8P_()
    turtle.speed(Xd_f)

@S8yIW((chr((37 + 75)) + (str() + ('ix' + 'el'))))
def tQW_6(x4m63, h02_D, i1gB5):
    'g8g1Vc_02h_6_997Kp_7a74A8Z48O'
    mM27GA4(i1gB5, AAia51, int((((-1.4540753100862016 + 0.5582345487381373) + (0.3477104157928228 + 0.5827026872508334)) * 0)), (chr(112) + (str() + ('ixe' + 'l'))))
    E29Q_ = eval(i1gB5)
    wr8W0_ = turtle.getcanvas()
    (uW_8u, Ny0F42c) = (wr8W0_.winfo_width(), wr8W0_.winfo_height())
    if (not hasattr(tQW_6, (str() + (('i' + 'ma') + ('' + 'ge'))))):
        J8P_()
        tQW_6.image = tkinter.PhotoImage(width=uW_8u, height=Ny0F42c)
        wr8W0_.create_image((int(((0.13144411458906513 + 0.7699067565308937) * 0)), int((((-1.4171758369412606 + 0.9469202586288186) + (0.596106059297958 + 0.3002294189046777)) * int(((0.39063642717264435 + 0.25031241355226164) * int((0.8100888599563434 * 0))))))), image=tQW_6.image, state=(('' + ('n' + 'o')) + (str() + ('' + 'rmal'))))
    IS0a0tuM = tQW_6.IS0a0tuM
    for j60722w_ in range(IS0a0tuM):
        for w_OHp in range(IS0a0tuM):
            (wj_l7_, V500q_i) = (((x4m63 * IS0a0tuM) + j60722w_), (Ny0F42c - ((h02_D * IS0a0tuM) + w_OHp)))
            if ((int(((0.37037867244853395 + 0.22885664722919352) * 0)) < wj_l7_ < uW_8u) and (int((((-0.9374323775178597 + 0.8288423524289522) + (-0.17013328159331242 + 0.40014408572964033)) * int(((0.21015800416999275 + 0.5595396638753752) * int((0.9529627409024952 * 0)))))) < V500q_i < Ny0F42c)):
                tQW_6.image.put(E29Q_, (wj_l7_, V500q_i))
tQW_6.IS0a0tuM = (((109 + -75) + (-101 + 28)) + ((138 + -50) + (21 + -69)))

@S8yIW(((('pi' + 'xe') + ('l' + 's')) + ('' + ('' + 'ize'))))
def wj_7Bb_(IS0a0tuM):
    'P0S5w_91eR4_qk0i208NPt__sUU25'
    d4mz222__(IS0a0tuM)
    if ((IS0a0tuM <= int((0.846076501408032 * 0))) or (not isinstance(IS0a0tuM, numbers.Integral))):
        raise Bx_ERNR6((((str() + ('Inv' + 'ali')) + (('d pi' + 'x') + ('el si' + 'ze: '))) + repl_str(IS0a0tuM)))
    tQW_6.IS0a0tuM = IS0a0tuM

@S8yIW(((('s' + 'cree') + ('n' + '_wid')) + ('t' + 'h')))
def Y0Qq():
    'B40_P5C4_2691vIRhzQ2__523k0I'
    return (turtle.getcanvas().winfo_width() // tQW_6.IS0a0tuM)

@S8yIW((('s' + ('c' + 're')) + (('en_' + 'heigh') + chr(116))))
def SMR1_M3_():
    'R3K6_LUP6NF80z_N__NP2_4_na_'
    return (turtle.getcanvas().winfo_height() // tQW_6.IS0a0tuM)
'pj306v9182_50__G_29___63'
v659 = (set(string.digits) | set((chr((-20 + 63)) + ('-' + '.'))))
xGfQ2bdM = (((set(((('!' + '$') + ('%' + '&*/:<=>')) + (chr(63) + ('@' + '^_~')))) | set(string.ascii_lowercase)) | set(string.ascii_uppercase)) | v659)
m7lNr6LT = set('"')
Y0KJ4 = set((('' + ('' + ' \t')) + ('\n' + '\r')))
l5G_47hb = set(((('()' + '[') + ('' + "]'")) + chr((147 + -51))))
ll7_D0Gz2 = (((Y0KJ4 | l5G_47hb) | m7lNr6LT) | {chr(((101 + -37) + (-4 + -16))), (str() + ('' + (',' + '@')))})
MCy826n = (l5G_47hb | {chr(((70 + 72) + (-79 + -17))), chr(44), (chr((-3 + 47)) + chr(64))})

def V_3N9Z143(Xd_f):
    'Fe_T38____R__H5__47454c'
    if (len(Xd_f) == int(((0.1222700964380079 + 0.7297903805895128) * 0))):
        return False
    for i1gB5 in Xd_f:
        if (i1gB5 not in xGfQ2bdM):
            return False
    return True

def nl6h0A(V92r, u3dhwH3):
    'qb976b6_6_0p_4_a_34RV9'
    while (u3dhwH3 < len(V92r)):
        i1gB5 = V92r[u3dhwH3]
        if (i1gB5 == chr((141 + -82))):
            return (None, len(V92r))
        elif (i1gB5 in Y0KJ4):
            u3dhwH3 += (((-135 + 97) + (-35 + 14)) + ((26 + 73) + (-118 + 79)))
        elif (i1gB5 in l5G_47hb):
            if (i1gB5 == chr(((78 + -85) + (140 + -40)))):
                i1gB5 = chr(((92 + -84) + (-20 + 53)))
            if (i1gB5 == chr(((137 + -6) + (-124 + 84)))):
                i1gB5 = chr(40)
            return (i1gB5, (u3dhwH3 + (((146 + 2) + (-37 + -56)) + ((-140 + 16) + (10 + 60)))))
        elif (i1gB5 == chr((92 + -57))):
            return (V92r[u3dhwH3:(u3dhwH3 + (((-43 + 49) + (-175 + 88)) + ((63 + 28) + (47 + -55))))], min((u3dhwH3 + (((171 + -63) + (-38 + -49)) + ((76 + -7) + (-76 + -12)))), len(V92r)))
        elif (i1gB5 == chr((99 + -55))):
            if (((u3dhwH3 + (((-114 + -45) + (114 + -28)) + ((173 + -84) + (-70 + 55)))) < len(V92r)) and (V92r[(u3dhwH3 + (((-100 + 91) + (-117 + 73)) + ((246 + -93) + (-12 + -87))))] == chr((151 + -87)))):
                return (('' + (',' + chr(64))), (u3dhwH3 + (((135 + -47) + (-4 + 10)) + ((27 + -83) + (-1 + -35)))))
            return (i1gB5, (u3dhwH3 + (((124 + -42) + (-120 + 46)) + ((-140 + 38) + (76 + 19)))))
        elif (i1gB5 in m7lNr6LT):
            if (((u3dhwH3 + (((10 + 44) + (-49 + 72)) + ((47 + -70) + (35 + -88)))) < len(V92r)) and (V92r[(u3dhwH3 + (((155 + -11) + (-60 + -16)) + (int((0.4266070367626609 * 0)) + (-153 + 86))))] == i1gB5)):
                return ((i1gB5 + i1gB5), (u3dhwH3 + (((-26 + -21) + (-45 + 54)) + ((89 + 23) + (-20 + -52)))))
            M_rde_ = (bytes(V92r[u3dhwH3:], encoding=(('u' + 't') + (str() + ('f-' + '8')))),)
            qF635Og_ = tokenize.tokenize(iter(M_rde_).__next__)
            next(qF635Og_)
            l6eJ9_Yt = next(qF635Og_)
            if (l6eJ9_Yt.type != tokenize.STRING):
                raise ValueError(((('' + 'inval') + ('id str' + 'ing: {')) + (str() + ('0' + '}'))).format(l6eJ9_Yt.string))
            return (l6eJ9_Yt.string, (l6eJ9_Yt.end[(((-52 + 26) + (-5 + -68)) + ((26 + 10) + (141 + -77)))] + u3dhwH3))
        else:
            G3o5_ = u3dhwH3
            while ((G3o5_ < len(V92r)) and (V92r[G3o5_] not in ll7_D0Gz2)):
                G3o5_ += (((-63 + 72) + (95 + -62)) + ((-67 + 23) + (10 + -7)))
            return (V92r[u3dhwH3:G3o5_], min(G3o5_, len(V92r)))
    return (None, len(V92r))

def Z9HhNRHBg(V92r):
    'cx58497_Z1x_25dWFrOU'
    kZ9O91gZy = []
    (R578oJ, Y49w) = nl6h0A(V92r, int((((-0.36329799071050006 + 0.044872201474065676) + (-0.34907189311602493 + 0.9946153473926396)) * int((0.48047328143078116 * 0)))))
    while (R578oJ is not None):
        if (R578oJ in MCy826n):
            kZ9O91gZy.append(R578oJ)
        elif ((R578oJ == ('' + ('#' + 't'))) or (R578oJ.lower() == (chr((78 + 38)) + (str() + ('' + 'rue'))))):
            kZ9O91gZy.append(True)
        elif ((R578oJ == (str() + ('#' + chr(102)))) or (R578oJ.lower() == (chr((15 + 87)) + ('' + ('al' + 'se'))))):
            kZ9O91gZy.append(False)
        elif (R578oJ == (str() + (str() + ('' + 'nil')))):
            kZ9O91gZy.append(R578oJ)
        elif (R578oJ[int((((0.13871659856700969 + 0.362115172244741) + (-0.02329156806926047 + 0.09563326713337539)) * int(((0.7090583986372945 + 0.18545730941590055) * int((0.5348629831662969 * 0))))))] in xGfQ2bdM):
            E93_r3A_N = False
            if (R578oJ[int((((-0.4742085003941151 + 0.5167355209054884) + (-0.2691682323200766 + 0.8241431765227916)) * int(((-0.8021649846944167 + 0.9018751835710455) * 0))))] in v659):
                try:
                    kZ9O91gZy.append(int(R578oJ))
                    E93_r3A_N = True
                except ValueError:
                    try:
                        kZ9O91gZy.append(float(R578oJ))
                        E93_r3A_N = True
                    except ValueError:
                        pass
            if (not E93_r3A_N):
                if V_3N9Z143(R578oJ):
                    kZ9O91gZy.append(R578oJ.lower())
                else:
                    raise ValueError(((('invalid n' + 'umeral or s') + ('' + 'ymbol: {0')) + '}').format(R578oJ))
        elif (R578oJ[0] in m7lNr6LT):
            kZ9O91gZy.append(R578oJ)
        else:
            print(((('w' + 'arn') + ('in' + 'g: invalid')) + ((' to' + 'ken') + (': ' + '{0}'))).format(R578oJ), file=sys.stderr)
            print((('' + (' ' + ' ')) + (chr(32) + chr(32))), V92r, file=sys.stderr)
            print((chr(32) * (Y49w + (((87 + -4) + (-36 + -44)) + int(((0.28643253741712804 + 0.06579697703147636) * int((0.34303438741543946 * 0))))))), chr((4 + 90)), file=sys.stderr)
        (R578oJ, Y49w) = nl6h0A(V92r, Y49w)
    return kZ9O91gZy

def h8C4_wo(input):
    'v1x9iUK66yi33CAbY8qE_o8a_OV_'
    return (Z9HhNRHBg(V92r) for V92r in input)

def GR4q_0VCF(input):
    'eY_gO2_KJGW2ZxZ1_9OPL6m'
    return len(list(itertools.chain(*h8C4_wo(input))))

def zX3m(*pO4_15tm):
    import argparse
    s_MJ8R = argparse.ArgumentParser(description=((('C' + 'ount') + (' Scheme to' + 'ken')) + (chr(115) + '.')))
    s_MJ8R.add_argument((('f' + ('i' + 'l')) + chr(101)), nargs=chr(((73 + -53) + (131 + -88))), type=argparse.FileType(chr((102 + 12))), default=sys.stdin, help=(('' + ('i' + 'n')) + (('p' + 'ut file to be ') + ('count' + 'ed'))))
    pO4_15tm = s_MJ8R.parse_args()
    print(((str() + ('co' + 'un')) + (str() + ('' + 'ted'))), GR4q_0VCF(pO4_15tm.file), ((('to' + 'k') + chr(101)) + ('n' + 's')))
'nAU1a4_8sXs9724H8fsIXK1'
__version__ = (chr(49) + (('' + '.2') + ('' + '.4')))

def Ol_93(q1Gj04i, j_84f34m, k6o5=None):
    'd2i99loE15F8Yi6_ior7'
    j_84f34m.stack.append(q1Gj04i)
    if tHw1_52C4(q1Gj04i):
        kZ9O91gZy = j_84f34m.k6_3(q1Gj04i)
        j_84f34m.stack.pop()
        return kZ9O91gZy
    elif YZD_64(q1Gj04i):
        j_84f34m.stack.pop()
        return q1Gj04i
    if (not eRY3S__9F(q1Gj04i)):
        raise Bx_ERNR6(((str() + ('' + 'ma')) + (('lfo' + 'rmed list:') + (' {' + '0}'))).format(repl_str(q1Gj04i)))
    (K60___u0, G_04) = (q1Gj04i.K60___u0, q1Gj04i.b21laz02)
    if (tHw1_52C4(K60___u0) and (K60___u0 in JUh97U)):
        kZ9O91gZy = JUh97U[K60___u0](G_04, j_84f34m)
        j_84f34m.stack.pop()
        return kZ9O91gZy
    else:
        L_F75il2M = Ol_93(K60___u0, j_84f34m)
        ZsA8(L_F75il2M)
        if isinstance(L_F75il2M, I3G__m37):
            q1Gj04i = L_F75il2M.b_8_6S268(G_04, j_84f34m)
            kZ9O91gZy = Ol_93(q1Gj04i, j_84f34m)
        else:
            pO4_15tm = G_04.map((lambda N__x3: Ol_93(N__x3, j_84f34m)))
            kZ9O91gZy = p94cc908(L_F75il2M, pO4_15tm, j_84f34m)
        j_84f34m.stack.pop()
        return kZ9O91gZy

def YZD_64(q1Gj04i):
    'bp00a0KXJ199i2R7a1UK'
    return ((b_fb7(q1Gj04i) and (not tHw1_52C4(q1Gj04i))) or (q1Gj04i is None))

def p94cc908(L_F75il2M, pO4_15tm, j_84f34m):
    'R8Q30EL7Ee_S394ez_641Y2ycn2'
    ZsA8(L_F75il2M)
    if isinstance(L_F75il2M, BuiltinProcedure):
        return L_F75il2M.z78b93m5(pO4_15tm, j_84f34m)
    else:
        D450_ = L_F75il2M.Yf___D(pO4_15tm, j_84f34m)
        return Y6Q1UdEv(L_F75il2M.K7328_, D450_)

def Y6Q1UdEv(h_9621_8, j_84f34m):
    'KBw_3__Vd_9i645___7_2Kl_1'
    Q33jkQ = None
    while (h_9621_8 is not nil):
        P_s_o = (h_9621_8.b21laz02 is nil)
        Q33jkQ = Ol_93(h_9621_8.K60___u0, j_84f34m, P_s_o)
        h_9621_8 = h_9621_8.b21laz02
    return Q33jkQ

class wO_5_eY_(object):
    'FiD96_3g058x__2WH_93d242_a_l'

    def __init__(z9ox6N_Q1, K8H12q_2):
        'vF7ruQ5hV_Z8_ih62q50'
        z9ox6N_Q1.HR8m6f12 = {
            
        }
        z9ox6N_Q1.K8H12q_2 = K8H12q_2
        if z9ox6N_Q1.K8H12q_2:
            z9ox6N_Q1.stack = z9ox6N_Q1.K8H12q_2.stack
        else:
            z9ox6N_Q1.stack = []

    def __repr__(z9ox6N_Q1):
        if (z9ox6N_Q1.K8H12q_2 is None):
            return ((('<Glo' + 'bal ') + ('Fr' + 'a')) + ('' + ('me' + '>')))
        Xd_f = sorted([((chr(123) + chr(48)) + ('}' + (': {' + '1}'))).format(u3dhwH3, fV_b8O_) for (u3dhwH3, fV_b8O_) in z9ox6N_Q1.HR8m6f12.items()])
        return (('' + ('<' + '{{{0}}} -> {')) + (str() + ('1}' + '>'))).format((str() + (str() + ('' + ', '))).join(Xd_f), repr(z9ox6N_Q1.K8H12q_2))

    def l__XN67C(z9ox6N_Q1, Mdy_J00_, Q33jkQ):
        'XB_5E2_b04T2_b9N506XK7c_45l'
        z9ox6N_Q1.HR8m6f12[Mdy_J00_] = Q33jkQ

    def k6_3(z9ox6N_Q1, Mdy_J00_):
        'V6_26667J80137OYMN6_5Cs1_18VH'
        l0E808fa = z9ox6N_Q1
        while (l0E808fa is not None):
            if (Mdy_J00_ in l0E808fa.HR8m6f12):
                return l0E808fa.HR8m6f12[Mdy_J00_]
            l0E808fa = l0E808fa.K8H12q_2
        raise Bx_ERNR6((chr((211 + -94)) + (('nknown id' + 'ent') + ('ifier:' + ' {0}'))).format(Mdy_J00_))

    def q_F_c4208(z9ox6N_Q1, Mdy_J00_, Q33jkQ):
        'F6zj_l812q_175__131s8Y_3_'
        l0E808fa = z9ox6N_Q1
        while (l0E808fa is not None):
            if (Mdy_J00_ in l0E808fa.HR8m6f12):
                l0E808fa.HR8m6f12[Mdy_J00_] = Q33jkQ
                return
            l0E808fa = l0E808fa.K8H12q_2
        raise Bx_ERNR6(((('unknow' + 'n') + ('' + ' ide')) + (('n' + 'tifie') + ('r: ' + '{0}'))).format(Mdy_J00_))

    def wDS6k8__n(z9ox6N_Q1, i0_5i_, uA_92):
        'hL2ia1Lo_H4n1Z__3c285_t5g_7Y'
        RXA_0__ = wO_5_eY_(z9ox6N_Q1)
        while isinstance(i0_5i_, Pair):
            if (uA_92 is nil):
                raise Bx_ERNR6(((('too' + ' few arguments to functi') + ('on' + ' c')) + (('' + 'al') + chr(108))))
            RXA_0__.l__XN67C(i0_5i_.K60___u0, uA_92.K60___u0)
            (i0_5i_, uA_92) = (i0_5i_.b21laz02, uA_92.b21laz02)
        if (i0_5i_ != nil):
            RXA_0__.l__XN67C(i0_5i_, uA_92)
        elif (uA_92 != nil):
            raise Bx_ERNR6(((('too ' + 'many ') + ('' + 'arg')) + (('' + 'ument') + ('s to functi' + 'on call'))))
        return RXA_0__

class Q_X_(object):
    'FdHK6_7F7__s6rY20Nv7223'

def D0afe_8A(x4m63):
    return isinstance(x4m63, Q_X_)

class BuiltinProcedure(Q_X_):
    'dV_250074_6524s__2Q2'

    def __init__(z9ox6N_Q1, H_5yXx_, jTKv=False, C4ht_2N8='builtin'):
        z9ox6N_Q1.C4ht_2N8 = C4ht_2N8
        z9ox6N_Q1.H_5yXx_ = H_5yXx_
        z9ox6N_Q1.jTKv = jTKv

    def __str__(z9ox6N_Q1):
        return ((str() + ('#' + '[{')) + (str() + ('' + '0}]'))).format(z9ox6N_Q1.C4ht_2N8)

    def z78b93m5(z9ox6N_Q1, pO4_15tm, j_84f34m):
        'pBQ1R_aN6_8Y8967ae6_87_'
        if (not eRY3S__9F(pO4_15tm)):
            raise Bx_ERNR6(((('argumen' + 'ts are not i') + ('' + 'n ')) + (('a l' + 'is') + ('t: {0' + '}'))).format(pO4_15tm))
        OaJ2s6 = []
        while (pO4_15tm is not nil):
            OaJ2s6.append(pO4_15tm.K60___u0)
            pO4_15tm = pO4_15tm.b21laz02
        if z9ox6N_Q1.jTKv:
            OaJ2s6.append(j_84f34m)
        try:
            return z9ox6N_Q1.H_5yXx_(*OaJ2s6)
        except TypeError as r8882eH:
            raise Bx_ERNR6(((('incorrect n' + 'umber of ') + chr(97)) + (('r' + 'gu') + ('ments: {' + '0}'))).format(z9ox6N_Q1))

class LambdaProcedure(Q_X_):
    'y3_3y4247Mu___3Op_u73'
    C4ht_2N8 = ((('' + '[l') + 'a') + (('mbd' + 'a') + chr(93)))

    def __init__(z9ox6N_Q1, i0_5i_, K7328_, j_84f34m):
        'FM_047509r969y_4Qd_6_w4'
        z9ox6N_Q1.i0_5i_ = i0_5i_
        z9ox6N_Q1.K7328_ = K7328_
        z9ox6N_Q1.j_84f34m = j_84f34m

    def Yf___D(z9ox6N_Q1, pO4_15tm, j_84f34m):
        'u6_30vUTw_dG_W34jd2_wSEq'
        return z9ox6N_Q1.j_84f34m.wDS6k8__n(z9ox6N_Q1.i0_5i_, pO4_15tm)

    def __str__(z9ox6N_Q1):
        return str(Pair(((('l' + 'a') + ('m' + 'bd')) + 'a'), Pair(z9ox6N_Q1.i0_5i_, z9ox6N_Q1.K7328_)))

    def __repr__(z9ox6N_Q1):
        return ((('' + 'Lam') + ('' + 'bdaPro')) + (('cedure({0' + '},') + (' {1}, {2}' + ')'))).format(repr(z9ox6N_Q1.i0_5i_), repr(z9ox6N_Q1.K7328_), repr(z9ox6N_Q1.j_84f34m))

class I3G__m37(LambdaProcedure):
    'LvpsJ4AT508r193e_3U01'

    def b_8_6S268(z9ox6N_Q1, YM0Q, j_84f34m):
        'Zq_6X4_PmtY8PY_PaC36C7g5_'
        return R__D_zN(z9ox6N_Q1, YM0Q, j_84f34m)

def P3o_y4ooX(k4101, n6719M):
    'u3_P_35_0_55JM0Av7_86U_Pk_Y2'
    for (C4ht_2N8, H_5yXx_, vpw0e53C6) in n6719M:
        k4101.l__XN67C(C4ht_2N8, BuiltinProcedure(H_5yXx_, C4ht_2N8=vpw0e53C6))

def vf3LM_(h_9621_8, j_84f34m):
    'c8_3JE_9355m77d1k0I5_xTnCM'
    H1tLi(h_9621_8, (((260 + -81) + (-48 + -34)) + ((-134 + -24) + (-8 + 71))))
    oo3s83M3 = h_9621_8.K60___u0
    if tHw1_52C4(oo3s83M3):
        H1tLi(h_9621_8, (((-51 + -14) + (74 + -97)) + ((175 + -59) + (24 + -50))), (((5 + 90) + (-42 + -18)) + ((-30 + 6) + (-96 + 87))))
        Q33jkQ = Ol_93(h_9621_8.b21laz02.K60___u0, j_84f34m)
        j_84f34m.l__XN67C(oo3s83M3, Q33jkQ)
        return oo3s83M3
    elif (isinstance(oo3s83M3, Pair) and tHw1_52C4(oo3s83M3.K60___u0)):
        C4ht_2N8 = oo3s83M3.K60___u0
        i0_5i_ = oo3s83M3.b21laz02
        K7328_ = h_9621_8.b21laz02
        Q33jkQ = B2Q3(Pair(i0_5i_, K7328_), j_84f34m)
        Q33jkQ.C4ht_2N8 = C4ht_2N8
        j_84f34m.l__XN67C(C4ht_2N8, Q33jkQ)
        return C4ht_2N8
    else:
        n_3_x5s = (oo3s83M3.K60___u0 if isinstance(oo3s83M3, Pair) else oo3s83M3)
        raise Bx_ERNR6(((('' + 'no') + ('n-symbol: ' + '{')) + (chr(48) + '}')).format(n_3_x5s))

def e70_L(h_9621_8, j_84f34m):
    'r35_U1_9sm9B_5LmO58_i4q4'
    H1tLi(h_9621_8, (((156 + -88) + (1 + 19)) + ((-141 + 1) + (-45 + 98))), (((-63 + 23) + (52 + 31)) + ((-58 + -55) + (31 + 40))))
    return h_9621_8.K60___u0

def t15_k51__(h_9621_8, j_84f34m):
    'Bsch382_u3__71_4V_ZUg_130dM_Z'
    H1tLi(h_9621_8, (((-63 + 20) + (0 + -46)) + ((36 + -35) + (4 + 85))))
    return Y6Q1UdEv(h_9621_8, j_84f34m)

def B2Q3(h_9621_8, j_84f34m):
    'a6T14uqv2K_42EO53_y_188F'
    H1tLi(h_9621_8, (((-166 + 1) + (125 + -41)) + ((88 + 0) + (-90 + 85))))
    i0_5i_ = h_9621_8.K60___u0
    X9N4f(i0_5i_)
    return LambdaProcedure(i0_5i_, h_9621_8.b21laz02, j_84f34m)

def MEm3gK35(h_9621_8, j_84f34m):
    'js03U_9_8_5vY_0Ba965'
    H1tLi(h_9621_8, (((103 + -79) + (-36 + 7)) + ((-52 + 14) + (58 + -13))), (((-116 + 47) + (-105 + 83)) + ((85 + 83) + (-121 + 47))))
    if C_u1m_(Ol_93(h_9621_8.K60___u0, j_84f34m)):
        return Ol_93(h_9621_8.b21laz02.K60___u0, j_84f34m, True)
    elif (len(h_9621_8) == (((59 + 0) + (-143 + 66)) + ((20 + 35) + (24 + -58)))):
        return Ol_93(h_9621_8.b21laz02.b21laz02.K60___u0, j_84f34m, True)

def Cpr77_p9(h_9621_8, j_84f34m):
    'n__M26D95527_38_3__B_'
    Q33jkQ = True
    while (h_9621_8 is not nil):
        P_s_o = (h_9621_8.b21laz02 is nil)
        Q33jkQ = Ol_93(h_9621_8.K60___u0, j_84f34m, P_s_o)
        if y02j4E(Q33jkQ):
            return Q33jkQ
        h_9621_8 = h_9621_8.b21laz02
    return Q33jkQ

def v5__sJa8(h_9621_8, j_84f34m):
    'R2__5_5_06c4m_0YS0rtF6_x3d'
    Q33jkQ = False
    while (h_9621_8 is not nil):
        P_s_o = (h_9621_8.b21laz02 is nil)
        Q33jkQ = Ol_93(h_9621_8.K60___u0, j_84f34m, P_s_o)
        if C_u1m_(Q33jkQ):
            return Q33jkQ
        h_9621_8 = h_9621_8.b21laz02
    return Q33jkQ

def EH_I7l_X(h_9621_8, j_84f34m):
    'c7V2l_Vf0_l51Y627__DKALW'
    while (h_9621_8 is not nil):
        c0477_70 = h_9621_8.K60___u0
        H1tLi(c0477_70, (((120 + -20) + (-127 + 47)) + ((-75 + -9) + (155 + -90))))
        if (c0477_70.K60___u0 == (('e' + ('' + 'ls')) + chr(101))):
            pW5_4 = True
            if (h_9621_8.b21laz02 != nil):
                raise Bx_ERNR6(((('' + 'els') + ('e ' + 'must be ')) + (str() + ('la' + 'st'))))
        else:
            pW5_4 = Ol_93(c0477_70.K60___u0, j_84f34m)
        if C_u1m_(pW5_4):
            if (len(c0477_70) == (((26 + -65) + (-37 + 47)) + ((0 + -33) + (-26 + 89)))):
                return pW5_4
            else:
                return Y6Q1UdEv(c0477_70.b21laz02, j_84f34m)
        h_9621_8 = h_9621_8.b21laz02

def F2Q86(h_9621_8, j_84f34m):
    'SYCT99mOW26tk09_q3z__57Y7OA_2'
    H1tLi(h_9621_8, (((-27 + 54) + (-21 + 57)) + ((-194 + 69) + (21 + 43))))
    u8mEZ = SheK6O_6(h_9621_8.K60___u0, j_84f34m)
    return Y6Q1UdEv(h_9621_8.b21laz02, u8mEZ)

def SheK6O_6(HR8m6f12, j_84f34m):
    'Irb6639_3_80Y8_oM46_I'
    if (not eRY3S__9F(HR8m6f12)):
        raise Bx_ERNR6(((str() + ('' + 'bad')) + (('' + ' bi') + ('ndings ' + 'list in let form'))))
    (z_eUs, r2c_4e) = (nil, nil)
    while (HR8m6f12 is not nil):
        Dg043G29 = HR8m6f12.K60___u0
        H1tLi(Dg043G29, (((-58 + 67) + (-33 + 68)) + ((-135 + 68) + (111 + -86))), (((22 + -55) + (36 + -12)) + ((119 + -71) + (39 + -76))))
        C4ht_2N8 = Dg043G29.K60___u0
        Z8HS3_ = Ol_93(Dg043G29.b21laz02.K60___u0, j_84f34m)
        z_eUs = Pair(C4ht_2N8, z_eUs)
        r2c_4e = Pair(Z8HS3_, r2c_4e)
        HR8m6f12 = HR8m6f12.b21laz02
    X9N4f(z_eUs)
    return j_84f34m.wDS6k8__n(z_eUs, r2c_4e)

def O__37_U6(h_9621_8, j_84f34m):
    'Io3_l36e41k0B__81Bu884_7R'
    H1tLi(h_9621_8, (((-100 + 87) + (7 + 10)) + ((74 + -70) + (77 + -83))))
    oo3s83M3 = h_9621_8.K60___u0
    if (isinstance(oo3s83M3, Pair) and tHw1_52C4(oo3s83M3.K60___u0)):
        C4ht_2N8 = oo3s83M3.K60___u0
        i0_5i_ = oo3s83M3.b21laz02
        K7328_ = h_9621_8.b21laz02
        X9N4f(i0_5i_)
        Q33jkQ = I3G__m37(i0_5i_, K7328_, j_84f34m)
        Q33jkQ.C4ht_2N8 = C4ht_2N8
        j_84f34m.l__XN67C(C4ht_2N8, Q33jkQ)
        return C4ht_2N8
    else:
        raise Bx_ERNR6((('i' + ('mprope' + 'r ')) + (('fo' + 'r') + ('m for define' + '-macro'))))

def XfROn0_2(h_9621_8, j_84f34m):
    'xXSfx_k4m0i0___29S8t2v5jo633'

    def R510(Z8HS3_, j_84f34m, G05G_):
        'P69ZDKy_H9_1_7m_589553M7T'
        if (not hV8_81(Z8HS3_)):
            return Z8HS3_
        if (Z8HS3_.K60___u0 == ((('u' + 'n') + ('' + 'qu')) + (('o' + 't') + chr(101)))):
            G05G_ -= (((109 + -74) + (35 + 24)) + ((-3 + -76) + (7 + -21)))
            if (G05G_ == int(((0.052044117094403264 + 0.2713351367084297) * int((0.4094342583300935 * 0))))):
                h_9621_8 = Z8HS3_.b21laz02
                H1tLi(h_9621_8, (((75 + -11) + (-164 + 82)) + ((60 + 22) + (-46 + -17))), (((-89 + 42) + (96 + -63)) + ((19 + 8) + (-51 + 39))))
                return Ol_93(h_9621_8.K60___u0, j_84f34m)
        elif (Z8HS3_.K60___u0 == (str() + (('qu' + 'as') + ('iq' + 'uote')))):
            G05G_ += (((176 + -92) + (-23 + 5)) + ((75 + -60) + (-178 + 98)))
        K60___u0 = R510(Z8HS3_.K60___u0, j_84f34m, G05G_)
        b21laz02 = R510(Z8HS3_.b21laz02, j_84f34m, G05G_)
        return Pair(K60___u0, b21laz02)
    H1tLi(h_9621_8, (((173 + -43) + (-98 + 24)) + ((-19 + 54) + (-41 + -49))), (((161 + -94) + (59 + -25)) + ((-54 + 47) + (-82 + -11))))
    return R510(h_9621_8.K60___u0, j_84f34m, (int((0.8721401905760111 * 0)) + ((-116 + 20) + (63 + 34))))

def gf62(h_9621_8, j_84f34m):
    raise Bx_ERNR6(((('unquote o' + 'uts') + ('ide o' + 'f q')) + (('' + 'ua') + ('si' + 'quote'))))

def I84_xF98(h_9621_8, j_84f34m):
    'f2_f7T24n_O82oS69_u_P0226E6Lq'
    H1tLi(h_9621_8, (((196 + -59) + (-29 + -14)) + ((-84 + 44) + (-44 + -8))))
    C4ht_2N8 = h_9621_8.K60___u0
    if (not tHw1_52C4(C4ht_2N8)):
        raise Bx_ERNR6((((('bad ' + 'ar') + 'g') + (str() + ('' + 'ument: '))) + repl_str(C4ht_2N8)))
    Q33jkQ = Ol_93(h_9621_8.b21laz02.K60___u0, j_84f34m)
    j_84f34m.q_F_c4208(C4ht_2N8, Q33jkQ)

def XfROn0_2(h_9621_8, j_84f34m):
    'B90678bW8j7oCCp16_8H_C_8'
    H1tLi(h_9621_8, (((-81 + 75) + (160 + -67)) + ((-94 + -57) + (24 + 41))), (((-85 + 24) + (142 + -61)) + ((-2 + 74) + (-174 + 83))))
    (Z8HS3_, FnZ2t9_) = R510(h_9621_8.K60___u0, j_84f34m)
    if FnZ2t9_:
        L23___ = ((('unquote-splicing ' + 'not') + (' in list templ' + 'ate')) + ('' + (': {0' + '}')))
        raise Bx_ERNR6(L23___.format(h_9621_8.K60___u0))
    return Z8HS3_

def R510(Z8HS3_, j_84f34m, G05G_=1):
    'mhl_6YV__7qg_885___553f5__'
    if hV8_81(Z8HS3_):
        if (Z8HS3_.K60___u0 in (('' + ('u' + ('n' + 'quote'))), (('u' + ('n' + 'quote-')) + (('sp' + 'l') + ('' + 'icing'))))):
            G05G_ -= (((-171 + 61) + (17 + 42)) + ((188 + -78) + (-1 + -57)))
            if (G05G_ == int(((-0.18415085883856808 + 0.20765991291641006) * 0))):
                h_9621_8 = Z8HS3_.b21laz02
                H1tLi(h_9621_8, (((-73 + -53) + (-12 + 54)) + ((8 + 41) + (45 + -9))), (((-37 + 48) + (92 + -42)) + ((-106 + -25) + (23 + 48))))
                o7z0Om = Ol_93(h_9621_8.K60___u0, j_84f34m)
                FnZ2t9_ = (Z8HS3_.K60___u0 == ((chr(117) + ('n' + 'quote-spl')) + (('i' + 'ci') + ('' + 'ng'))))
                if (FnZ2t9_ and (not eRY3S__9F(o7z0Om))):
                    L23___ = ((('' + 'unquot') + chr(101)) + (('-splicing u' + 's') + ('ed on' + ' non-list: {0}')))
                    raise Bx_ERNR6(L23___.format(o7z0Om))
                return (o7z0Om, FnZ2t9_)
        elif (Z8HS3_.K60___u0 == (chr((113 + 0)) + (('ua' + 'siqu') + ('o' + 'te')))):
            G05G_ += (((-5 + 30) + (-28 + 27)) + ((117 + -49) + (-19 + -72)))
        (K60___u0, FnZ2t9_) = R510(Z8HS3_.K60___u0, j_84f34m, G05G_)
        (b21laz02, k6o5) = R510(Z8HS3_.b21laz02, j_84f34m, G05G_)
        if FnZ2t9_:
            if (b21laz02 is not nil):
                return (j2_V6xZ_G(K60___u0, b21laz02), False)
            return (K60___u0, False)
        return (Pair(K60___u0, b21laz02), False)
    else:
        return (Z8HS3_, False)
JUh97U = {
    ((str() + ('' + 'an')) + chr((135 + -35))): Cpr77_p9,
    (chr(98) + (('' + 'eg') + ('' + 'in'))): t15_k51__,
    ('c' + (str() + ('' + 'ond'))): EH_I7l_X,
    (chr((28 + 72)) + (('e' + 'fin') + chr(101))): vf3LM_,
    (chr(105) + chr((159 + -57))): MEm3gK35,
    ((chr(108) + ('' + 'am')) + (('' + 'bd') + 'a')): B2Q3,
    (str() + (('' + 'le') + chr(116))): F2Q86,
    (str() + (str() + ('o' + 'r'))): v5__sJa8,
    (str() + (str() + ('quo' + 'te'))): e70_L,
    (('d' + ('' + 'ef')) + (('in' + 'e-') + ('macr' + 'o'))): O__37_U6,
    ((('q' + 'u') + ('' + 'asi')) + (('' + 'qu') + ('o' + 'te'))): XfROn0_2,
    (('u' + chr(110)) + (('' + 'quo') + ('t' + 'e'))): gf62,
    ((chr(115) + 'e') + (str() + ('t' + '!'))): I84_xF98,
    ('' + (('un' + 'quot') + ('e-s' + 'plicing'))): gf62,
}

def H1tLi(q1Gj04i, min, max=float('inf')):
    'f_2841eO95Q8Z7f01X_3_77_C9N0_'
    if (not eRY3S__9F(q1Gj04i)):
        raise Bx_ERNR6(((chr(98) + (('a' + 'dly formed expression') + (':' + ' '))) + repl_str(q1Gj04i)))
    q5__5E = len(q1Gj04i)
    if (q5__5E < min):
        raise Bx_ERNR6((('' + ('too few o' + 'peran')) + (('d' + 's ') + ('in fo' + 'rm'))))
    elif (q5__5E > max):
        raise Bx_ERNR6(((('' + 'to') + ('' + 'o many o')) + (('pe' + 'rands i') + ('n ' + 'form'))))

def X9N4f(i0_5i_):
    'tbf45_T_I42g_BL_S074VS305zD'
    V_99y = set()

    def z__4p0M2_(Mdy_J00_):
        if (not tHw1_52C4(Mdy_J00_)):
            raise Bx_ERNR6(((('' + 'no') + ('n-s' + 'y')) + (('mb' + 'ol: {') + ('' + '0}'))).format(Mdy_J00_))
        if (Mdy_J00_ in V_99y):
            raise Bx_ERNR6((str() + (('duplicat' + 'e symbol: {') + ('' + '0}'))).format(Mdy_J00_))
        V_99y.add(Mdy_J00_)
    while isinstance(i0_5i_, Pair):
        z__4p0M2_(i0_5i_.K60___u0)
        i0_5i_ = i0_5i_.b21laz02
    if (i0_5i_ != nil):
        z__4p0M2_(i0_5i_)

def ZsA8(L_F75il2M):
    'L0jB207Bl585_6EDM26_'
    if (not D0afe_8A(L_F75il2M)):
        raise Bx_ERNR6(((('{' + '0} is') + (' n' + 'o')) + (('t' + ' ca') + ('llable: {' + '1}'))).format(type(L_F75il2M).__name__.lower(), repl_str(L_F75il2M)))

class MuProcedure(Q_X_):
    'zj_4d3_MJ7_zk1vs9BzL_k193Qk8'
    C4ht_2N8 = ('[' + (str() + ('mu' + ']')))

    def __init__(z9ox6N_Q1, i0_5i_, K7328_):
        'q0Us3uVXl5__Qp___E85Iw_9zK0_'
        z9ox6N_Q1.i0_5i_ = i0_5i_
        z9ox6N_Q1.K7328_ = K7328_

    def Yf___D(z9ox6N_Q1, pO4_15tm, j_84f34m):
        'jWA5C142U3r1J60A6K_a0nfG4X_X'
        return j_84f34m.wDS6k8__n(z9ox6N_Q1.i0_5i_, pO4_15tm)

    def __str__(z9ox6N_Q1):
        return str(Pair(('' + (str() + ('' + 'mu'))), Pair(z9ox6N_Q1.i0_5i_, z9ox6N_Q1.K7328_)))

    def __repr__(z9ox6N_Q1):
        return ((('MuPr' + 'ocedur') + ('' + 'e({0}')) + (str() + (', ' + '{1})'))).format(repr(z9ox6N_Q1.i0_5i_), repr(z9ox6N_Q1.K7328_))

def q__9l_QxD(h_9621_8, j_84f34m):
    'G6948_p547h8D2220_jP745__rq_'
    H1tLi(h_9621_8, (((74 + 2) + (-133 + 99)) + ((-16 + 51) + (-101 + 26))))
    i0_5i_ = h_9621_8.K60___u0
    X9N4f(i0_5i_)
    return MuProcedure(i0_5i_, h_9621_8.b21laz02)
JUh97U[(str() + ('m' + 'u'))] = q__9l_QxD

class Promise(object):
    'AnK3_J__P_549hv99_n2'

    def __init__(z9ox6N_Q1, wR__, j_84f34m):
        z9ox6N_Q1.wR__ = wR__
        z9ox6N_Q1.j_84f34m = j_84f34m

    def q_8_4(z9ox6N_Q1):
        if (z9ox6N_Q1.wR__ is not None):
            z9ox6N_Q1.Q33jkQ = Ol_93(z9ox6N_Q1.wR__, z9ox6N_Q1.j_84f34m.wDS6k8__n(nil, nil))
            z9ox6N_Q1.wR__ = None
        return z9ox6N_Q1.Q33jkQ

    def __str__(z9ox6N_Q1):
        return ((str() + ('#[' + 'pr')) + (('' + 'omis') + ('e ({' + '0}forced)]'))).format(((str() + (('' + 'not') + ' ')) if (z9ox6N_Q1.wR__ is not None) else str()))

def K_77_M42(h_9621_8, j_84f34m):
    'a68_6S5__g3_47u6Ct6__xn_'
    H1tLi(h_9621_8, (((91 + -93) + (83 + -8)) + ((99 + -78) + (-174 + 81))), (((88 + 74) + (-164 + 72)) + ((14 + 7) + (-121 + 31))))
    return Promise(h_9621_8.K60___u0, j_84f34m)

def Z75zE3_(h_9621_8, j_84f34m):
    'guY4f184K7MO_O5lX94x8Ab9R82x_'
    H1tLi(h_9621_8, (((124 + -44) + (-120 + 86)) + ((-23 + -92) + (78 + -7))), (((171 + -62) + (-117 + 46)) + ((78 + -60) + (-129 + 75))))
    return Pair(Ol_93(h_9621_8.K60___u0, j_84f34m), K_77_M42(h_9621_8.b21laz02, j_84f34m))
JUh97U[((('' + 'cons-s') + ('t' + 're')) + (chr(97) + 'm'))] = Z75zE3_
JUh97U[('d' + (('el' + 'a') + 'y'))] = K_77_M42

class HtJ0_q_5y(object):
    'Y063_9y52_4J0l_92H3852W15'

    def __init__(z9ox6N_Q1, q1Gj04i, j_84f34m):
        z9ox6N_Q1.q1Gj04i = q1Gj04i
        z9ox6N_Q1.j_84f34m = j_84f34m

def R__D_zN(L_F75il2M, pO4_15tm, j_84f34m):
    'B_9_832_PM9GeFuNdz668U_'
    Z8HS3_ = p94cc908(L_F75il2M, pO4_15tm, j_84f34m)
    if isinstance(Z8HS3_, HtJ0_q_5y):
        return Ol_93(Z8HS3_.q1Gj04i, Z8HS3_.j_84f34m)
    else:
        return Z8HS3_

def X_54PnSx3(Avf6_):
    'rAL2UK5aOw2_I_3wLg457Zx'

    def mow4478_9(q1Gj04i, j_84f34m, P_s_o=False):
        'q6i8_Y2_2F922527fzm__784Xl8'
        if (P_s_o and (not tHw1_52C4(q1Gj04i)) and (not YZD_64(q1Gj04i))):
            return HtJ0_q_5y(q1Gj04i, j_84f34m)
        kZ9O91gZy = HtJ0_q_5y(q1Gj04i, j_84f34m)
        while isinstance(kZ9O91gZy, HtJ0_q_5y):
            (q1Gj04i, j_84f34m) = (kZ9O91gZy.q1Gj04i, kZ9O91gZy.j_84f34m)
            kZ9O91gZy = Avf6_(q1Gj04i, j_84f34m)
        return kZ9O91gZy
    return mow4478_9

def y9a_4_v6r(H_5yXx_, Xd_f, j_84f34m):
    mM27GA4(H_5yXx_, D0afe_8A, int(((0.3007589289141729 + 0.6951600954709598) * 0)), ('' + (('' + 'ma') + 'p')))
    mM27GA4(Xd_f, eRY3S__9F, (((-156 + 45) + (100 + -37)) + ((56 + 49) + (-108 + 52))), ('m' + ('a' + 'p')))
    return Xd_f.map((lambda x4m63: R__D_zN(H_5yXx_, Pair(x4m63, nil), j_84f34m)))

def e1_p_TAb(H_5yXx_, Xd_f, j_84f34m):
    mM27GA4(H_5yXx_, D0afe_8A, int((((0.6488361577920511 + 0.16525774015554529) + (-0.8809313417543487 + 0.8837013239018559)) * int(((0.4520118081361093 + 0.33817498794665235) * int((0.39921628506859674 * 0)))))), (str() + (('fil' + 'te') + 'r')))
    mM27GA4(Xd_f, eRY3S__9F, (((-15 + -24) + (147 + -66)) + ((87 + -71) + (-84 + 27))), (str() + ('f' + ('il' + 'ter'))))
    (o6z1rt8, current) = (nil, nil)
    while (Xd_f is not nil):
        (wKHM___p1, Xd_f) = (Xd_f.K60___u0, Xd_f.b21laz02)
        if R__D_zN(H_5yXx_, Pair(wKHM___p1, nil), j_84f34m):
            if (o6z1rt8 is nil):
                o6z1rt8 = Pair(wKHM___p1, nil)
                current = o6z1rt8
            else:
                current.b21laz02 = Pair(wKHM___p1, nil)
                current = current.b21laz02
    return o6z1rt8

def xi2_097(H_5yXx_, Xd_f, j_84f34m):
    mM27GA4(H_5yXx_, D0afe_8A, int(((-0.17322652990842036 + 0.723970146406578) * 0)), (('' + ('' + 'redu')) + (chr(99) + 'e')))
    mM27GA4(Xd_f, (lambda x4m63: (x4m63 is not nil)), (((16 + -91) + (-40 + 87)) + ((-84 + 69) + (-7 + 51))), ((('re' + 'd') + ('' + 'uc')) + chr((186 + -85))))
    mM27GA4(Xd_f, eRY3S__9F, (((67 + -10) + (0 + -51)) + ((-24 + -22) + (44 + -3))), (chr((84 + 30)) + (('edu' + 'c') + 'e')))
    (Q33jkQ, Xd_f) = (Xd_f.K60___u0, Xd_f.b21laz02)
    while (Xd_f is not nil):
        Q33jkQ = R__D_zN(H_5yXx_, u722nW_0(Q33jkQ, Xd_f.K60___u0), j_84f34m)
        Xd_f = Xd_f.b21laz02
    return Q33jkQ

def yl960_(mFrjl389, j_84f34m, Fek021c_C=False, h_O5a=False, cBQ_4=False, F35c_Kh=(), p3pC_=False):
    'S0d1ix77D_p96n8InO_21GZN9X2X'
    if cBQ_4:
        try:
            Bx_8(((str() + ('sc' + 'h')) + (('e' + 'me_l') + ('i' + 'b'))), True, j_84f34m)
        except Bx_ERNR6:
            pass
        for X_5c in F35c_Kh:
            Bx_8(X_5c, True, j_84f34m)
    while True:
        try:
            Y__t = mFrjl389()
            while Y__t.F49_454J:
                wR__ = A1_Au9(Y__t)
                kZ9O91gZy = Ol_93(wR__, j_84f34m)
                if ((not h_O5a) and (kZ9O91gZy is not None)):
                    print(repl_str(kZ9O91gZy))
        except (Bx_ERNR6, SyntaxError, ValueError, RuntimeError) as r8882eH:
            if p3pC_:
                if isinstance(r8882eH, SyntaxError):
                    r8882eH = Bx_ERNR6(r8882eH)
                    raise r8882eH
            R1w9(j_84f34m)
            if (isinstance(r8882eH, RuntimeError) and (((('maximum rec' + 'ur') + ('sion d' + 'ept')) + (('h' + ' exc') + ('eede' + 'd'))) not in getattr(r8882eH, ((str() + ('a' + 'r')) + ('' + ('' + 'gs'))))[int(((-0.07063585932279004 + 0.2899608446938349) * int((0.4287521484016077 * 0))))])):
                raise
            elif isinstance(r8882eH, RuntimeError):
                print((str() + (('Error' + ': m') + ('aximum recursion dept' + 'h exceeded'))))
            else:
                print(('' + (('Er' + 'r') + ('' + 'or:'))), r8882eH)
        except KeyboardInterrupt:
            if (not cBQ_4):
                raise
            j_84f34m.stack = []
            print()
            print(((('' + 'Key') + ('boardInterru' + 'p')) + chr((183 + -67))))
            if (not Fek021c_C):
                return
        except EOFError:
            print()
            return
b01450ef = {
    ((chr(115) + 'e') + chr((208 + -92))): (chr((43 + 72)) + (chr(101) + ('' + 't!'))),
}

def R1w9(j_84f34m):
    print(((str() + ('Traceback (m' + 'ost re')) + (('ce' + 'nt') + ('' + ' call last):'))))
    for (fB9u, q1Gj04i) in enumerate(j_84f34m.stack):
        print(((str() + (str() + ('' + '  '))) + str(fB9u)), repl_str(q1Gj04i), sep=chr(((184 + -89) + (-160 + 74))))
    j_84f34m.stack[:] = []

def Bx_8(*pO4_15tm):
    'Z0NvK3_dVpCF9ej_5_qz1M1k'
    if (not ((((6 + -89) + (-15 + 57)) + ((-19 + -37) + (180 + -81))) <= len(pO4_15tm) <= (((-7 + -5) + (-91 + 62)) + ((33 + 85) + (-94 + 20))))):
        h_9621_8 = pO4_15tm[:(- (((44 + -21) + (69 + -8)) + ((-120 + 58) + (-56 + 35))))]
        raise Bx_ERNR6(((('"l' + 'oa') + chr(100)) + (('" given incorrect number' + ' of a') + ('rgumen' + 'ts: {0}'))).format(len(h_9621_8)))
    D8Ec4_01 = pO4_15tm[0]
    h_O5a = (pO4_15tm[(((-157 + 78) + (165 + -65)) + ((26 + -5) + (-65 + 24)))] if (len(pO4_15tm) > (((46 + 38) + (-99 + 75)) + ((-5 + -87) + (13 + 21)))) else True)
    j_84f34m = pO4_15tm[(- (((16 + -96) + (32 + -23)) + ((9 + 34) + (12 + 17))))]
    if AAia51(D8Ec4_01):
        D8Ec4_01 = eval(D8Ec4_01)
    mM27GA4(D8Ec4_01, tHw1_52C4, 0, (chr(108) + (('o' + 'a') + 'd')))
    with a__FY9J(D8Ec4_01) as kpdV0906P:
        Ky5Q00 = kpdV0906P.readlines()
    pO4_15tm = ((Ky5Q00, None) if h_O5a else (Ky5Q00,))

    def mFrjl389():
        return bNn5(*pO4_15tm)
    mA79m = j_84f34m.stack[:]
    j_84f34m.stack[:] = []
    yl960_(mFrjl389, j_84f34m, h_O5a=h_O5a, p3pC_=True)
    j_84f34m.stack[:] = mA79m

def a__FY9J(X_5c):
    'rme4_f_3jz1XO_w0tuK6g7_'
    try:
        return open(X_5c)
    except IOError as c_vb:
        if X_5c.endswith((chr((-37 + 83)) + (chr(115) + ('' + 'cm')))):
            raise Bx_ERNR6(str(c_vb))
    try:
        return open((X_5c + (('' + ('' + '.s')) + (chr(99) + 'm'))))
    except IOError as c_vb:
        raise Bx_ERNR6(str(c_vb))

def lCk2CY0():
    'd7_9g831l2as_D___aNh16'
    j_84f34m = wO_5_eY_(None)
    j_84f34m.l__XN67C(((('e' + 'v') + 'a') + chr(108)), BuiltinProcedure(Ol_93, True, (chr(101) + (('' + 'va') + chr(108)))))
    j_84f34m.l__XN67C(((('a' + 'pp') + chr(108)) + 'y'), BuiltinProcedure(R__D_zN, True, ((('a' + 'pp') + chr(108)) + chr((128 + -7)))))
    j_84f34m.l__XN67C((str() + ('l' + ('oa' + 'd'))), BuiltinProcedure(Bx_8, True, (str() + (('l' + 'o') + ('a' + 'd')))))
    j_84f34m.l__XN67C(('' + (('proced' + 'ure') + '?')), BuiltinProcedure(D0afe_8A, False, (('p' + 'r') + ('o' + ('ce' + 'dure?')))))
    j_84f34m.l__XN67C((('m' + 'a') + 'p'), BuiltinProcedure(y9a_4_v6r, True, (chr((187 + -78)) + ('a' + 'p'))))
    j_84f34m.l__XN67C(((('f' + 'ilt') + 'e') + chr((71 + 43))), BuiltinProcedure(e1_p_TAb, True, ((str() + ('fi' + 'lt')) + (chr(101) + 'r'))))
    j_84f34m.l__XN67C(((chr(114) + ('e' + 'du')) + ('c' + chr(101))), BuiltinProcedure(xi2_097, True, ('r' + (('e' + 'duc') + chr(101)))))
    j_84f34m.l__XN67C(((('u' + 'n') + ('de' + 'fi')) + (chr(110) + ('' + 'ed'))), None)
    j_84f34m.stack = []
    P3o_y4ooX(j_84f34m, Y6__)
    return j_84f34m

def zX3m(*argv):
    import argparse
    s_MJ8R = argparse.ArgumentParser(description=((('' + 'CS') + (' 61A ' + 'Scheme Inte')) + (('rpre' + 't') + ('e' + 'r'))))
    import __main__
    if (((chr(108) + ('o' + 'g')) + (str() + ('' + 'ic'))) in __main__.__file__):
        O_Yu = ((('Lo' + 'g') + 'i') + chr((147 + -48)))
    else:
        O_Yu = ((str() + ('S' + 'c')) + ('' + ('hem' + 'e')))
    version = __main__.__version__
    s_MJ8R.add_argument((('-' + '-') + (('ve' + 'rsio') + 'n')), action=((('vers' + 'i') + 'o') + chr((141 + -31))), version=(chr((50 + 73)) + chr((191 + -66))).format(version))
    s_MJ8R.add_argument((str() + ('-' + ('loa' + 'd'))), ('' + ('-' + 'i')), action=((('s' + 't') + ('o' + 're_t')) + (('r' + 'u') + chr(101))), help=((('r' + 'un') + (' fi' + 'l')) + (('e ' + 'inter') + ('activ' + 'ely'))))
    s_MJ8R.add_argument((chr((153 + -51)) + (('' + 'il') + chr(101))), nargs=chr((81 + -18)), type=argparse.FileType(chr((29 + 85))), default=None, help=((('S' + 'che') + ('me fi' + 'l')) + (('e to' + ' r') + ('' + 'un'))))
    pO4_15tm = s_MJ8R.parse_args()
    mFrjl389 = tjf7_65Al
    Fek021c_C = True
    F35c_Kh = []
    if (pO4_15tm.file is not None):
        if pO4_15tm.load:
            F35c_Kh.append(getattr(pO4_15tm.file, (str() + (('' + 'nam') + chr(101)))))
        else:
            Ky5Q00 = pO4_15tm.file.readlines()

            def mFrjl389():
                return bNn5(Ky5Q00)
            Fek021c_C = False
    print(((('We' + 'lcom') + ('' + 'e to')) + ((' t' + 'he CS 61A') + (' {} Interpreter (ve' + 'rsion {})'))).format(O_Yu, version))
    yl960_(mFrjl389, lCk2CY0(), cBQ_4=True, Fek021c_C=Fek021c_C, F35c_Kh=F35c_Kh)
    G2w38w_P5()

