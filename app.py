from flask import Flask, request
from models import test_crypt
from models import ClassEncription, ClassEncriptionSmall

Crypto = test_crypt.Crypto()
ClassEncription = ClassEncription.encription()
ClassEncriptionSmall = ClassEncriptionSmall.encription()


app = Flask(__name__)


@app.route('/ecription', methods=['GET', 'POST'])
def ecription():
    text = request.form['text']
    encrTxt = Crypto.rot13(text)
    return encrTxt


# @app.route('/ecription_tab1', methods=['GET', 'POST'])
# def ecription_tab1():
#     ClassEncription.selectDataTab1()
#     ClassEncription.updateTab1()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab2', methods=['GET', 'POST'])
# def ecription_tab2():
#     ClassEncription.selectDataTab2()
#     ClassEncription.updateTab2()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab3', methods=['GET', 'POST'])
# def ecription_tab3():
#     ClassEncription.selectDataTab3()
#     ClassEncription.updateTab3()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab4', methods=['GET', 'POST'])
# def ecription_tab4():
#     ClassEncription.selectDataTab4()
#     ClassEncription.updateTab4()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab5', methods=['GET', 'POST'])
# def ecription_tab5():
#     ClassEncription.selectDataTab5()
#     ClassEncription.updateTab5()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab6', methods=['GET', 'POST'])
# def ecription_tab6():
#     ClassEncription.selectDataTab6()
#     ClassEncription.updateTab6()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab7', methods=['GET', 'POST'])
# def ecription_tab7():
#     ClassEncription.selectDataTab7()
#     ClassEncription.updateTab7()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab8', methods=['GET', 'POST'])
# def ecription_tab8():
#     ClassEncription.selectDataTab8()
#     ClassEncription.updateTab8()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab9', methods=['GET', 'POST'])
# def ecription_tab9():
#     ClassEncription.selectDataTab9()
#     ClassEncription.updateTab9()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab10', methods=['GET', 'POST'])
# def ecription_tab10():
#     ClassEncription.selectDataTab10()
#     ClassEncription.updateTab10()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab11', methods=['GET', 'POST'])
# def ecription_tab11():
#     ClassEncription.selectDataTab11()
#     ClassEncription.updateTab11()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab12', methods=['GET', 'POST'])
# def ecription_tab12():
#     ClassEncription.selectDataTab12()
#     ClassEncription.updateTab12()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab13', methods=['GET', 'POST'])
# def ecription_tab13():
#     ClassEncription.selectDataTab13()
#     ClassEncription.updateTab13()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab14', methods=['GET', 'POST'])
# def ecription_tab14():
#     ClassEncription.selectDataTab14()
#     ClassEncription.updateTab14()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab15', methods=['GET', 'POST'])
# def ecription_tab15():
#     ClassEncription.selectDataTab15()
#     ClassEncription.updateTab15()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab16', methods=['GET', 'POST'])
# def ecription_tab16():
#     ClassEncription.selectDataTab16()
#     ClassEncription.updateTab16()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab17', methods=['GET', 'POST'])
# def ecription_tab17():
#     ClassEncription.selectDataTab17()
#     ClassEncription.updateTab17()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab18', methods=['GET', 'POST'])
# def ecription_tab18():
#     ClassEncription.selectDataTab18()
#     ClassEncription.updateTab18()
#     return ClassEncription.response
#
#
# @app.route('/ecription_tab19', methods=['GET', 'POST'])
# def ecription_tab19():
#     ClassEncription.selectDataTab19()
#     ClassEncription.updateTab19()
#     return ClassEncription.response

@app.route('/ecription_tab20', methods=['GET', 'POST'])
def ecription_tab20():
    ClassEncription.selectDataTab20()
    ClassEncription.updateTab20()
    return ClassEncription.response

@app.route('/ecription_tab21', methods = ['GET', 'POST'])
def ecription_tab21():
    ClassEncription.selectDataTab21()
    ClassEncription.updateTab21()
    return ClassEncription.response

@app.route('/ecription_tab22', methods=['GET', 'POST'])
def ecription_tab22():
    ClassEncription.selectDataTab22()
    ClassEncription.updateTab22()
    return ClassEncription.response

@app.route('/ecription_tab23', methods=['GET', 'POST'])
def ecription_tab23():
    ClassEncription.selectDataTab23()
    ClassEncription.updateTab23()
    return ClassEncription.response

@app.route('/ecription_tab24', methods=['GET', 'POST'])
def ecription_tab24():
    ClassEncription.selectDataTab24()
    ClassEncription.updateTab24()
    return ClassEncription.response

@app.route('/ecription_tab25', methods=['GET', 'POST'])
def ecription_tab25():
    ClassEncription.selectDataTab25()
    ClassEncription.updateTab25()
    return ClassEncription.response
@app.route('/ecription_tab26', methods=['GET', 'POST'])
def ecription_tab26():
    ClassEncription.selectDataTab26()
    ClassEncription.updateTab26()
    return ClassEncription.response

@app.route('/ecription_tab27', methods=['GET', 'POST'])
def ecription_tab27():
    ClassEncription.selectDataTab27()
    ClassEncription.updateTab27()
    return ClassEncription.response

@app.route('/ecription_tab28', methods=['GET', 'POST'])
def ecription_tab28():
    ClassEncription.selectDataTab28()
    ClassEncription.updateTab28()
    return ClassEncription.response

@app.route('/ecription_tab29', methods=['GET', 'POST'])
def ecription_tab29():
    ClassEncription.selectDataTab29()
    ClassEncription.updateTab29()
    return ClassEncription.response

@app.route('/ecription_tab30', methods=['GET', 'POST'])
def ecription_tab30():
    ClassEncription.selectDataTab30()
    ClassEncription.updateTab30()
    return ClassEncription.response

@app.route('/ecription_tab31', methods=['GET', 'POST'])
def ecription_tab31():
    ClassEncription.selectDataTab31()
    ClassEncription.updateTab31()
    return ClassEncription.response

@app.route('/ecription_tab32', methods=['GET', 'POST'])
def ecription_tab32():
    ClassEncription.selectDataTab32()
    ClassEncription.updateTab32()
    return ClassEncription.response

@app.route('/ecription_tab33', methods=['GET', 'POST'])
def ecription_tab33():
    ClassEncription.selectDataTab33()
    ClassEncription.updateTab33()
    return ClassEncription.response

@app.route('/ecription_tab34', methods=['GET', 'POST'])
def ecription_tab34():
    ClassEncription.selectDataTab34()
    ClassEncription.updateTab34()
    return ClassEncription.response

@app.route('/ecription_tab35', methods=['GET', 'POST'])
def ecription_tab35():
    ClassEncription.selectDataTab35()
    ClassEncription.updateTab35()
    return ClassEncription.response

@app.route('/ecription_tab36', methods=['GET', 'POST'])
def ecription_tab36():
    ClassEncription.selectDataTab36()
    ClassEncription.updateTab36()
    return ClassEncription.response

@app.route('/ecription_tab37', methods=['GET', 'POST'])
def ecription_tab37():
    ClassEncription.selectDataTab37()
    ClassEncription.updateTab37()
    return ClassEncription.response\

@app.route('/ecription_tab38', methods=['GET', 'POST'])
def ecription_tab38():
    ClassEncription.selectDataTab38()
    ClassEncription.updateTab38()
    return ClassEncription.response
@app.route('/ecription_tab39', methods=['GET', 'POST'])
def ecription_tab39():
    ClassEncription.selectDataTab39()
    ClassEncription.updateTab39()
    return ClassEncription.response
@app.route('/ecription_tab40', methods=['GET', 'POST'])
def ecription_tab40():
    ClassEncription.selectDataTab40()
    ClassEncription.updateTab40()
    return ClassEncription.response
@app.route('/ecription_tab41', methods=['GET', 'POST'])
def ecription_tab41():
    ClassEncription.selectDataTab41()
    ClassEncription.updateTab41()
    return ClassEncription.response



if __name__ == '__main__':
    app.run()
