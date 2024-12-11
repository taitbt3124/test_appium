import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

def main():
    # Create a test suite
    # suite = unittest.defaultTestLoader.discover(start_dir='tests', pattern='training_route.py')
    # Create a blank suit
    suite = unittest.TestSuite()
    # Add more file to suit
    # suite.addTest(unittest.TestLoader().loadTestsFromName('tests.login.Login'))
    # suite.addTest(unittest.TestLoader().loadTestsFromName('tests.introduce_and_guide_video.TestViewIntroduceAndGuideVideo'))
    # suite.addTest(unittest.TestLoader().loadTestsFromName('tests.watch_free_video.FreeVideo'))
    # suite.addTest(unittest.TestLoader().loadTestsFromName('tests.training_route.TestViewTraningRoute'))
    # suite.addTest(unittest.TestLoader().loadTestsFromName('tests.video_in_route.Video_route'))
    suite.addTest(unittest.TestLoader().loadTestsFromName('tests.watch_all_video.WatchAllVideo'))

    # Run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    main()
  