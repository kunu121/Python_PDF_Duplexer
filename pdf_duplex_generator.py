from PyPDF2 import PdfReader, PdfWriter

def long_side_flip(pdf_reader):
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    for page_number in range(len(pdf_reader.pages)):
        if page_number % 2 == 0:
            pdf_writer_front.add_page(pdf_reader.pages[page_number])
        else:
            pdf_writer_back.add_page(pdf_reader.pages[page_number])

    return pdf_writer_front, pdf_writer_back

def short_side_flip(pdf_reader):
    pdf_writer_front = PdfWriter()
    pdf_writer_back = PdfWriter()

    for page_number in range(1, len(pdf_reader.pages), 2):
        pdf_writer_front.add_page(pdf_reader.pages[page_number])
        pdf_writer_back.add_page(pdf_reader.pages[page_number - 1])

    return pdf_writer_front, pdf_writer_back

def main():
    input_file_path = input("Enter the path of the PDF file: ")

    with open(input_file_path, "rb") as file:
        pdf_reader = PdfReader(file)

        option = input("Choose an option:\n1. Long Side Flip\n2. Short Side Flip\n")

        if option == "1":
            pdf_writer_front, pdf_writer_back = long_side_flip(pdf_reader)
        elif option == "2":
            pdf_writer_front, pdf_writer_back = short_side_flip(pdf_reader)
        else:
            print("Invalid option. Please choose 1 or 2.")
            return

        with open("front_pages.pdf", "wb") as front_file:
            pdf_writer_front.write(front_file)

        with open("back_pages.pdf", "wb") as back_file:
            pdf_writer_back.write(back_file)

        print("PDF files generated successfully.")

if __name__ == "__main__":
    main()
