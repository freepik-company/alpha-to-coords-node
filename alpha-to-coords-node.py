from nodes import Node


class ImageToArrayNode(Node):
    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "image": ("IMAGE",),  # Define the input type as an image
            }
        }

    @staticmethod
    def OUTPUT_TYPES():
        return {
            "array": ("LIST",),  # Define the output type as an array (list)
        }

    def process(self, image):
        """
        Processes the input image and converts it to an array.

        Args:
            image: The input image (likely in a format such as a PIL Image or NumPy array).

        Returns:
            dict: A dictionary containing the "array" output.
        """

        # Return the result as a dictionary
        return {"array": []}
