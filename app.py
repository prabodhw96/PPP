import streamlit as st

import awesome_streamlit as ast
import converter
import cap_map

ast.core.services.other.set_logging_format()

PAGES = {
	"Salary Converter": converter,
	"Map": cap_map
}

def main():
	#st.markdown("<h1 style='text-align: center;'>NPI RL</h1>", unsafe_allow_html=True)
	st.sidebar.title("Navigation")
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))

	page = PAGES[selection]

	with st.spinner(f"Loading {selection}..."):
		ast.shared.components.write_page(page)

if __name__ == "__main__":
	main()