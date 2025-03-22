import torch
import torchvision.utils as vutils
import streamlit as st

class Generator(torch.nn.Module):
    def __init__(self, nz):
        super(Generator, self).__init__()
        self.main = torch.nn.Sequential(
            torch.nn.ConvTranspose2d(nz, 512, 4, 1, 0, bias=False),
            torch.nn.BatchNorm2d(512),
            torch.nn.ReLU(True),
            torch.nn.ConvTranspose2d(512, 256, 4, 2, 1, bias=False),
            torch.nn.BatchNorm2d(256),
            torch.nn.ReLU(True),
            torch.nn.ConvTranspose2d(256, 128, 4, 2, 1, bias=False),
            torch.nn.BatchNorm2d(128),
            torch.torch.nn.ReLU(True),
            torch.nn.ConvTranspose2d(128, 64, 4, 2, 1, bias=False),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(True),
            torch.nn.ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
            torch.nn.Tanh()
        )

    def forward(self, input):
        return self.main(input)

# Load the model
nz = 100
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
generator = Generator(nz).to(device)
generator.load_state_dict(torch.load("generator.pth", map_location=device))
generator.eval()

# Streamlit UI
st.title("This Anime Face Does Not Exist")
st.write("Click the button to generate a new anime face!")

if st.button("Generate Image"):
    noise = torch.randn(1, 100, 1, 1, device=device)
    fake_image = generator(noise).detach().cpu()
    vutils.save_image(fake_image, "generated.png", normalize=True)
    st.image("generated.png", caption="AI-generated anime face")
