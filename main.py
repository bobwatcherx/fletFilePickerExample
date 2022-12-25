from flet import *
import shutil
def main(page:Page):

	youlocation_file = Text("")

	# CREATE FUNCTION OPEN FILE
	def dialog_picker(e:FilePickerResultEvent):
		for x in e.files:
			shutil.copy(x.name,f"myUploads/{x.name}")
			# SET LOCATION FOLDER IMAGE
			youlocation_file.value = f"myUploads/{x.name}"
			youlocation_file.update()






	Mypick = FilePicker(on_result=dialog_picker)
	page.overlay.append(Mypick)


	page.add(
		Column([
			ElevatedButton("Insert file",
		on_click=lambda _: Mypick.pick_files()
			),
		youlocation_file

			])

		)

flet.app(target=main)