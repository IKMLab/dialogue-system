from DSMachine.dataset.data_helper import SentimentDataTransformer
from DSMachine.sentiment.sentiment_classify import RNNSentimentClassifier
from DSMachine.trainer.supervised_trainer import ClassifierTrainer

def main():
    data_transformer = SentimentDataTransformer(dataset_path='dataset/Weibo/weibo_with_sentiment_tags.data',
                                                emote_meta_path='dataset/Weibo/emote/sentiment_class.txt',
                                                use_cuda=True,
                                                char_based=True)

    classifier = RNNSentimentClassifier(embedding_size=data_transformer.vocab_size, hidden_size=512, output_size=4, layers=2)
    classifier = classifier.cuda()
    trainer = ClassifierTrainer(data_transformer ,classifier)
    trainer.train(epochs=3000, batch_size=128, pretrained=True)

if __name__ == '__main__':
    main()