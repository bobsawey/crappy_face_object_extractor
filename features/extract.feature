Feature: showing off behave

  Scenario: extract portraits from images
     Given we have images in images_for_extraction
      When we run python3 extract.py
      Then images with very imperfectly extracted portraits will appeaar in extracted_portraits
