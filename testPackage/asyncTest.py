import asyncio  # Python 3.3부터 소개된 비동기 지원 모듈입니다.

import aiohttp  # asyncio를 사용하여 HTTP 요청을 하기 위해 사용합니다.

import aiofiles  # asyncio를 사용하여 파일 입출력을 하기 위해 사용합니다.

# async def는 해당 함수를 코루틴으로 만들어줍니다.
# i: int 라는 부분은 type annotation입니다. 본 소스의 동작에는 일체의 영향을 주지 않습니다.
async def download(i: int):
    async with aiohttp.ClientSession() as session:  # requests의 Session 클래스 같은 역할입니다.
        # 실제 요청을 비동기적으로 발생시킵니다.
        async with session.get('http://www.randomtext.me/api/lorem/p-1/32') as resp:
            # Python의 기본 open 함수는 비동기 입출력을 지원하지 않습니다. 그렇기에 외부 의존성을 씁니다.
            async with aiofiles.open('{}.txt'.format(i), 'w') as f:
                await f.write(await resp.text())  # 결과를 text로 불러와서 파일에 저장합니다.



# 요청 128개를 준비합니다.
# 만든 당시에는 아직 아무것도 일어나지 않고, 아랫줄의 asyncio.wait에 의해 동시에 실행됩니다.
tasks = [download(x) for x in range(128)]
# 실행..
asyncio.run(asyncio.wait(tasks))


