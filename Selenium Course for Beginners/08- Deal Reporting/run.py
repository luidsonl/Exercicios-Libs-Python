from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()# aceita parâmetros
    bot.select_place_to_go('Panama city')
    bot.select_checkin_checkout('2023-05-30', '2023-06-30')
    bot.search()
    bot.report_results()

input('Pressione enter para finalizar')