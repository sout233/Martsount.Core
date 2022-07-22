def xxx_rnd(rnd):
    if rnd==0:
        return ''
    elif rnd==1:
        return ''
    elif rnd==2:
        return ''
    elif rnd==3:
        return ''
    elif rnd==4:
        return ''


xxx = on_keyword(['','','',''],priority=50)
@xxx.handle()
async def xxx_handle(bot: Bot, event: Event):
    rnd = random.randint(0, 4)
    await xxx.finish(f'{xxx_rnd(rnd)}')
