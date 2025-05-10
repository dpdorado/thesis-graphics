from data.architectures_data import get_data as get_arch_data
from data.publications_data import get_data as get_pub_data
from data.preprocessing_data import get_data as get_prep_data
from data.augmentation_data import get_data as get_aug_data
from data.augmentation_technique_data import get_data as get_augtech_data
from data.classifiers_data import get_data as get_clf_data
from data.features_data import get_data as get_feat_data
from data.metrics_data import get_data as get_metrics_data
from data.classification_type_data import get_data as get_class_type_data
from data.dataset_publications_data import get_data as get_ds_pub_data
from data.datasets_top_data import get_data as get_top_ds_data
from data.datasets_top8_data import get_data as get_top8_ds_data
from data.datasets_public_private_totals_data import get_data as get_pp_ds_data

from categories.publications import Publications
from categories.generic import Category
from categories.datasets import Datasets


def main():
    Publications(**get_pub_data()).generate_charts()
    Datasets(**get_ds_pub_data()).generate_charts()
    Datasets(**get_top_ds_data(), name="top_datasets", title="Top datasets").generate_charts()
    Datasets(**get_top8_ds_data(), name="top8_datasets", title="Top 8 datasets").generate_charts()
    Datasets(**get_pp_ds_data(), name="pp_datasets", title="Top pp datasets").generate_charts()
    Category(**get_arch_data(), name="architectures", title="Arquitecturas").generate_charts()
    Category(**get_prep_data(), name="preprocessing", title="Técnicas de preprocesamiento").generate_charts()
    Category(**get_aug_data(), name="augmentation_si_no", title="Aumento de datos").generate_charts()
    Category(**get_augtech_data(), name="augmentation_technique", title="Tipo de técnica de aumento").generate_charts()
    Category(**get_clf_data(), name="classifiers", title="Modelos clasificadores").generate_charts()
    Category(**get_feat_data(), name="features", title="Técnicas de extracción").generate_charts()
    Category(**get_metrics_data(), name="metrics", title="Métricas").generate_charts()
    Category(**get_class_type_data(), name="classification_type", title="Tipos de clasificación").generate_charts()

if __name__ == "__main__":
    main()
