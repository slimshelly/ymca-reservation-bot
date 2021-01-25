# ymca-reservation-bot
- a bot to reserve swim times at the local ymca (is this cheating ?)

swimming at the ymca is insannnely competitive, slots book out the second they are available.
this custom bot, built with selenium, can book a time slot for you.

## running the bot - v1
you need to set the following variables/macros:
1. `SESSION_ID`: the ID of the `div` of the time slot (can find with inspect element)
2. `BOOKING_TIME`: the time the reservation should be booked (eg, if you're booking for 3pm 2 days from now, you bot should book the slot at 3pm today)
3.  `USERNAME` your username
4.  `PASSWORD` your password

the bot will countdown until the `BOOKING_TIME` and book

## running the bot - v2
you need to set the following variables/macros
1.  `USERNAME` your username
2.  `PASSWORD` your password

the bot will use today's date and the current time to find the next available time slot, 2 days from now, and count down in the background and book it for you.
