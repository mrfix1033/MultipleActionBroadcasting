# ActionMulticast by mrfix1033

## О программе

Программа позволяет вести трансляцию действий с одного компьютера на несколько других, используя локальную сеть.
Все действия выполняются немедленно. Пока поддерживается только Windows, 32/64 bit.

## Перед началом работы

Рекомендуется полностью изучить программу на 2-ух компьютерах, чтобы, если что, что-то поменять в коде, скомпилировать,
и только потом размещать на других клиентах

## Общие команды

`help` - показать все доступные команды\
`check_update` - проверить наличие обновлений\
`update` - обновить программу до последней версии\
`version` - посмотреть версию программы

## Команды клиента

`startup` add/remove - добавить/убрать программу из автозагрузки\
`restart` - перезапустить программу (потеряете 20МБ ОЗУ, также можно перезагрузить пк)\
`stop` - остановить программу

## Команды сервера

`startup` add/remove clients/server - добавить/убрать клиентам/серверу программу из автозагрузки\
`count` - выводит количество подключенных клиентов\
`clients_console` hide/show - скрыть/показать консоль у всех клиентов\
`find` <sound/video/all> <ip1 ip2 ip3...> - дать звуковой/видео/оба сигнал на IPs\
`update_all_clients` <путь к файлу> - отправляет file всем клиентам, они обновляются (но не перезапускаются).
Каждый клиент отправляет оповещение об успешном (или нет) обновлении.
При каждом таком сообщении выводится краткая количественная статистика такого формата
(успешно обновленные клиенты, ошибка при обновлении, неизвестно, (всего клиентов, которым было отправлено обновление))\
`update_all_clients_info` - показывает статистику по обновлению всех клиентов\
`restart` \<IP\>/server/all_clients/all - перезапустить программу на: определённом компьютере/сервере(здесь)/всех
клиентах/везде (потеряете 20МБ ОЗУ, также можно перезагрузить пк)\
`stop` \<IP\>/server/all_clients/all - остановить программу на: определённом компьютере/сервере(здесь)/всех
клиентах/везде

## Конфиг клиента

#### Маяк - оповещение всем компьютерам от сервера о его наличии в сети

`server_ip: null`\
`server_port: 10330`\
Для поиска сервера в **локальной** сети нужно установить server_ip в None. server_port игнорируется.
Для подключения к конкретному серверу (локальная/глобальная сеть (не тестировалось)) нужно задать server_ip и
server_port

`beacon_port: 10331`\
Порт для получения маяков сервера

`keycodes_to_hide_show_console: [165, 163, 161, 13]`\
Сочетание клавиш, которое необходимо зажать для скрытия/открытия окна консоли. Это клавиши RAlt, RCtrl, RShift, Enter

`start_hidden: false`\
Скрывать консоль при запуске?

`auto_enable_startup: false`
Добавлять программу при запуске в автозагрузку?

## Конфиг сервера

`ip: "0.0.0.0"`\
`port: 10330`\
IP и порт сервера

`beacon_port: 10331`\
На этот порт будут отправляться маяки

`beacon_interval: 3`\
Время в секундах между маяками

`auto_enable_startup: false`\
Добавлять программу при запуске в автозагрузку?

`find_sound_volume: 0.4`\
Громкость звука, который звучит при поиске (команда find sound с сервера)