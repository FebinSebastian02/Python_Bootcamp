from PyPDF2 import PdfMerger
import pikepdf

# An object is created from PdfMerger class
merger = PdfMerger()

for pdf in ["F:\Febin\@RPTU\Internship\Master's\Master's Degree Transcript.pdf", "F:\Febin\@RPTU\Internship\Master's\Matriculation Certificate.pdf",
            "F:\Febin\@RPTU\Internship\Mandatory Internship_Syllabus.pdf", "F:\Febin\@RPTU\Internship\Bachelor's\Bachelors Degree Certificate.pdf",
            "F:\Febin\@RPTU\Internship\Bachelor's\Bachelors Degree Transcript.pdf",
            "F:\Febin\@RPTU\Internship\Additional Documents\WorkExperience_Febin Sebastian.pdf",
            "F:\Febin\@RPTU\Internship\Additional Documents\B1_Goethe Certificate.pdf",
            "F:\Febin\@RPTU\Internship\Additional Documents\Driving license_Germany.pdf", "F:\Febin\@RPTU\Internship\Additional Documents\Residence Permit_Febin Sebastian.pdf",
            "F:\Febin\@RPTU\Internship\Additional Documents\Workpermit.pdf", "F:\Febin\@RPTU\Internship\Additional Documents\MatLab Onramp.pdf",
            "F:\Febin\@RPTU\Internship\Additional Documents\Simulink_Onramp.pdf"]:
    merger.append(pdf)

merger.write("F:\Febin\@RPTU\Internship\Additional Documents_Febin Sebastian.pdf")
merger.close()
