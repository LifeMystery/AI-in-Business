import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=3):
    """
    Summarize the given text using Latent Semantic Analysis (LSA).

    Args:
        text (str): The text to summarize.
        num_sentences (int, optional): The number of sentences to include in the summary. Defaults to 3.

    Returns:
        str: The summarized text, consisting of the specified number of sentences.
    """

    # Parse the text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Initialize the LSA summarizer
    summarizer = LsaSummarizer()
    
    # Generate the summary
    summary = summarizer(parser.document, num_sentences)
    
    # Join the sentences to form the final summary
    return ' '.join(str(sentence) for sentence in summary)

def save_summary_to_json(summary, filename='summary.json'):

    """
    Save the summarized text to a JSON file.

    Args:
        summary (str): The text summary to save.
        filename (str, optional): The name of the JSON file to save the summary. Defaults to 'summary.json'.

    Returns:
        None
    """

    # Create a dictionary to store the summary
    data = {
        'summary': summary
    }
    
    # Write the dictionary to a JSON file
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    # Example text to summarize
    text = """
    South Africa’s water security remains one of the most pressing issues for households and businesses, and continues to remain top of mind for investors.
    
    This is outlined in Coronation’s July 2024 Correspondent, where economist Marie Antelme and ESG analyst Leila Joseph say that “water security is arguably one of the most critical risks to South Africa’s social, economic, and political long-term future.”
    
    Households and businesses across South Africa are struggling with water stress worsened by climate change and municipal infrastructure challenges, impacting the availability of sufficient, usable water required to operate.
    
    The fund manager’s study showed that water security emerged as the most concerning environmental issue for their clients, with 78% of respondents indicating that this should be prioritised by investors in 2024.
    
    The Department of Water and Sanitation (DWS) has said that “South Africa is facing a number of water challenges and concerns, which include security of supply, environmental degradation, resource pollution, and the inefficient use of water, which are all among the chief causes of the supply deficit.
    
    Recently released reports by DWS — including the Green, Blue, and No Drop Reports – paint a concerning image of the current state of the provision of the essential resource, showing that at a countrywide average:
    
    
    51% of water provided has poor to bad microbiological water quality status;
    40.8% of water was lost due to leaks or was unaccounted for;
    67.6% of wastewater treatments failed to adequately process sewage and other wastes.
    According to another study by the department, “water demand is expected to sharply increase over the next 20 years while the water supply is likely to decline, therefore anticipating a projected supply deficit of 17% by 2030.”
    
    On top of examples of poor planning and management, significant underinvestment in infrastructure which has seen it rapidly deteriorate, vandalism and corruption, the water-scarce country’s risk is exacerbated by climate change.
    
    Antelme and Joseph highlight that with an average annual rainfall of just 460mm—less than half the global average—rainfall distribution is uneven and highly concentrated in just 8% of the land.
    """
    
    # Get the summary
    summary = summarize_text(text, num_sentences=5)
    
    # Print the summary
    print("Summary:")
    print(summary)
    
    # Save the summary to a JSON file
    save_summary_to_json(summary)
