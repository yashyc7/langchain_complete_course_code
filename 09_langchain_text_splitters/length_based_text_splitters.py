"""
Category 1: Length-based Text Splitters
What it means

Split text purely by character or token length, ignoring meaning or structure.

Used when:
• Structure is unknown
• Data is noisy
• You want predictable chunk sizes


Pros:
• Simple
• Fast

Cons:
• Can break sentences
• Weak semantic coherence

for eg text is 
Space exploration has led to incredible scientific discoveries.
From landing on the Moon to exploring Mars, humanity
continues to push the boundaries of what’s possible beyond our
planet.
These missions have not only expanded our knowledge of the
universe but have also contributed to advancements in
technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques tra
"""

from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

splitter = CharacterTextSplitter(separator='',chunk_size = 100, chunk_overlap=0)
#chunk overlap meaning how many characters is overlapped during character splitter


result = splitter.split_text(text)

print(result) #['Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the', "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type a", 'nd scrambled it to make a type specimen book. It has survived not only five centuries, but also the', 'leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s w', 'ith the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop p', 'ublishing software like Aldus PageMaker including versions of Lorem Ipsum.']
print (len(result)) #6 

# if we wanted to load the texts from pdf then 

loader = PyPDFLoader('kech102.pdf')

docs = loader.load()


new_result = splitter.split_documents(docs)

print(new_result)

# [
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="The rich diversity of chemical behaviour of different \nelements can be traced to the differences in",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="the internal \nstructure of atoms of these elements.\nUnit 2\nstr Uct Ure of atom\nAfter studying this u",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="nit you will be \nable to\n•\nknow about the discovery of\nelectron, proton \nand neutron and\ntheir chara",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="cteristics;\n• describe Thomson, Rutherford\nand Bohr atomic models;\n•\n understand the important featu",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="res \nof the qu\nantum mechanical model\nof atom;\n• understand nat\nure of\nelectromagnetic radiation and",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="Planck’s quantum theory;\n•\nexplain the \nphotoelectric effect\nand describe features of atomic\nspectr",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="a;\n•\nstate the de Broglie relation and\nHeisenberg uncertainty principle;\n• define\n\tan\tatomic\torbital",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="in\tterms\nof quantum numbers;\n• state aufbau \nprinciple, Pauli\nexclusion principle and Hund’s\nrule o",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="f maximum multiplicity; and\n• write\n\tthe\telectronic\tconfigurations\nof atoms.\nThe existence of atoms",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="has been proposed since the time \nof early Indian and Greek philosophers (400 B.C.) who \nwere of the",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="view that atoms are the fundamental building \nblocks of matter. According to them, the continued \ns",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="ubdivisions of matter would ultimately yield atoms \nwhich would not be further divisible. The word ‘",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="atom’  \nhas been derived from the Greek word ‘a-tomio’ which \nmeans ‘uncut-able’ or ‘non-divisible’.",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="These earlier ideas \nwere mere speculations and there was no way to test \nthem experimentally. Thes",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="e ideas remained dormant  for \na very long time and were revived again by scientists in \nthe ninetee",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="nth century.\nThe atomic theory of matter was first proposed \non\n\t a\t firm\t scientific \t basis \t by",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="John\t Dalton, \t a\t British \t\nschool\n teacher in 1808. His theory, called Dalton’s \natomic theory, re",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="garded the atom as the ultimate \nparticle\n\t of\t matter\t (Unit\t 1).\t Dalton’s\t atomic\t theory\t was\t\na",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="ble to explain the law of conservation of mass, law of \nconstant composition and \nlaw of multiple pr",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="oportion \nvery successfully. However, it failed to explain the results \nof many experiments, for exa",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="mple, it was known that \nsubstances like glass or ebonite when rubbed with silk \nor fur get electric",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="ally charged.\nIn this unit we start with the experimental observations \nmade by scientists towards t",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="he end of nineteenth and \nbeginning of twentieth century. These established that \natoms are made of",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="sub-atomic particles, i.e., electrons,  \nprotons and neutrons — a concept very different from \nthat",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 0,
#             "page_label": "1",
#         },
#         page_content="of\tDalton.\t\no bjectives\nUnit 2.indd   29 9/9/2022   4:28:07 PM\nReprint 2025-26",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="30\nchemistry\n2.1 Discovery of sUb-atomic \nParticles\nAn insight into the structure of atom was \nobtai",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="ned from the \nexperiments on electrical \ndischarge through gases. Before we discuss \nthese results w",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="e need to keep in mind a \nbasic rule regarding the behaviour of charged \nparticles : “Like charges r",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="epel each other and \nunlike charges attract each other”. \n2.1.1 Discovery of \nelectron \nIn 1830\n, Mi",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="chael Faraday showed that if \nelectricity is passed through a solution of an \nelectrolyte, chemical",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="reactions occurred at the \nelectrodes, which resulted in the liberation \nand deposition of matter at",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="the electrodes. \nHe formulated certain laws which you will \nstudy in Class XII. These results sugge",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="sted \nthe particulate nature of electricity.\nIn mid 1850s many scientists mainly \nFaraday began to s",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="tudy electrical discharge \nin partially evacuated tubes, known as \ncathode ray discharge tubes. It i",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="s depicted \nin Fig. 2.1. A cathode ray tube is made of \nglass containing two thin pieces of metal,",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="called electrodes, sealed in it. The electrical \ndischarge through the gases could be \nobserved only",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="at very low pressures and at \nvery high voltages. The pressure of different \ngases could be adjuste",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="d by evacuation of the \nglass\n\ttubes.\tWhen\tsufficiently \thigh\tvoltage\t\nis applied across the electro",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="des, current \nstarts\n\tflowing\tthrough\ta\tstream\tof\tparticles\t\nmoving in the tube from the negative \ne",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="lectrode \n(cathode) to the positive electrode \n(anode). These were called cathode rays or \ncathode r",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="ay particles.\n\tThe\tflow\tof\tcurrent\t\nfrom cathode to anode was further checked \nby making a hole in t",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="he anode and coating \nthe tube behind anode with phosphorescent \nmaterial \nzinc sulphide. When these",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="rays, \nafter passing through anode, strike the zinc \nsulphide coating, a bright spot is developed",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="on the coating [Fig. 2.1(b)].  \nFig. 2.1(a) A cathode ray discharge tube\nFig. 2.1(b)  A cathode ray",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="discharge tube with \nperforated anode\nThe results of these experiments are \nsummarised below.\n(i) Th",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="e ca\nthode rays start from cathode and \nmove towards the anode.\n(ii) These rays themselves are not v",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="isible \nbut their behaviour can be observed \nwith the help of certain kind of materials \n(fluorescen",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="t\n\t or\t phosphorescent)\t which\t\nglow when hit by them. Television \npicture tubes are cathode ray tub",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="es \nand television pi\nctures result due to \nfluorescence \t on\t the\t television \t screen\t\ncoated with",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="certain fluorescent or \nphosphorescent materials.\n(iii)\n In the absence of electrical or magnetic",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="field,\n\tthese\trays\ttravel\tin\tstraight\tlines\t\n(Fig. 2.2).\n(iv) In the presence of electrical or magne",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="tic \nfield,\n\tthe\tbehaviour\tof\tcathode\trays\tare\t\nsimilar to that expected from negatively \ncharged pa",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="rticles, suggesting that \nthe cath\node rays consist of negatively \ncharged particles, called electro",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="ns.\n(v) The characteristics of cathode rays \n(electrons) do not depend upon the \nUnit 2.indd   30 9/",
#     ),
#     Document(
#         metadata={
#             "producer": "PDFium",
#             "creator": "PDFium",
#             "creationdate": "D:20260211015658",
#             "source": "kech102.pdf",
#             "total_pages": 2,
#             "page": 1,
#             "page_label": "2",
#         },
#         page_content="9/2022   4:28:08 PM\nReprint 2025-26",
#     ),
# ]
