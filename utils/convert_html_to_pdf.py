#
import asyncio
import nest_asyncio
from pyppeteer import launch
import os
import json


def convert_html_to_pdf(links_data, pdf_dir):
    # link_dataのhrefのページを読み取り
    # pdfに変換して、ローカルの　.data/pdfs/　に保存する

    # nest_asyncioを適用
    nest_asyncio.apply()

    async def save_pdf(url, output_path):
        browser = await launch()
        page = await browser.newPage()
        # タイムアウトを120秒に設定し、waitUntilオプションをnetworkidle2に変更
        await page.goto(url, {'waitUntil': 'networkidle2', 'timeout': 120000})
        await page.pdf({'path': output_path, 'format': 'A4'})
        await browser.close()

    # 非同期関数を実行するためのラッパー関数
    async def save_all_pdfs(links_data):
        tasks = []
        for title, url in links_data.items():
            # ファイル名の設定（タイトルを使用）
            filename = title.replace(" ", "_").replace("/", "_") + '.pdf'
            filepath = os.path.join(pdf_dir, filename)
            # タスクの作成
            task = asyncio.create_task(save_pdf(url, filepath))
            tasks.append(task)
        # すべてのタスクを同時に実行
        await asyncio.gather(*tasks)

    # 非同期関数を実行
    asyncio.get_event_loop().run_until_complete(save_all_pdfs(links_data))
